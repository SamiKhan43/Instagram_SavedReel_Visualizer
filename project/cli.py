import sys
try:
    from .config import Paths, CSV_ENCODING
    from .processor import to_dataframe
    from .scraper import InstagramScraper
    from .visualization import write_markdown
    from .utils import extract_reel_urls
except ImportError:
    from config import Paths, CSV_ENCODING
    from processor import to_dataframe
    from scraper import InstagramScraper
    from visualization import write_markdown
    from utils import extract_reel_urls



def run(args) -> None:
    Paths.ensure_dirs_exist()
    if not Paths.validate_input():
        sys.exit(
            f"Put your Instagram export at {Paths.INPUT_FILE} "
            "before running the script."
        )

    print("1/4 Parsing saved_posts.json ...")

    urls = extract_reel_urls(Paths.INPUT_FILE)  

    if args.limit is not None:
        urls = urls[:args.limit]

    print(f"    Found {len(urls)} unique URLs")

    if not urls:
        sys.exit("No Instagram URLs found in the file.")

    print("2/4 Enriching via Apify ...")

    if args.skip_scrape:
        try:
            items = InstagramScraper.load_cached()
        except FileNotFoundError:
            sys.exit(
                "No cached results found. "
                "Run once without --skip-scrape first."
            )
    else:
        scraper = InstagramScraper()
        items = scraper.scrape_urls(urls)
        if items:
            scraper.save_cache(items)

    print(f"    Got {len(items)} results")

    print("3/4 Building CSV ...")

    df = to_dataframe(items)

    if df.empty:
        sys.exit(
            "Apify returned no data. "
            "Check your token/credits and that the reels are public."
        )

    df.to_csv(
        Paths.CSV_FILE,
        index=False,
        encoding=CSV_ENCODING
    )

    print(f"    Saved {Paths.CSV_FILE}")

    print("4/4 Generating Mermaid roadmap ...")

    write_markdown(df)

    print(f"    Saved {Paths.MD_FILE}\nDone ✅")


def build_parser():
    import argparse

    parser = argparse.ArgumentParser(
        description="Turn saved Instagram reels into a learning roadmap."
    )

    parser.add_argument(
        "--skip-scrape",
        action="store_true",
        help="reuse cached Apify results instead of scraping again"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="only process the first N reels"
    )

    return parser