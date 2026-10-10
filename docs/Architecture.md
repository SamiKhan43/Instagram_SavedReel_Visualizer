# How It Works

```mermaid
flowchart TD
    CMD["main.py → cli.py<br/>--skip-scrape, --limit"]
    IN[("saved_posts.json<br/>Instagram export")]
    P1["1. Parse export<br/>utils.extract_reel_urls"]
    S2A["2a. Scrape via Apify<br/>scraper.py (needs APIFY token)"]
    S2B["2b. Load cache<br/>apify_raw_results.json"]
    P3["3. Build and categorize<br/>processor.py"]
    CSV[("Enriched CSV<br/>data/outputs/")]
    P4["4. Generate roadmap<br/>visualization.py"]
    MD[("visual_roadmap.md<br/>Mermaid flowcharts")]

    CMD --> P1
    IN --> P1
    P1 -->|default| S2A
    P1 -->|--skip-scrape| S2B
    S2A --> P3
    S2B --> P3
    P3 --> CSV
    P3 --> P4
    P4 --> MD
```

## Steps

1. **Parse export:** reads `data/saved_posts.json` and collects unique reel URLs (`--limit N` keeps the first N).
2. **Enrich:** either scrape the URLs with Apify in batches (saving `apify_raw_results.json`), or reuse that cache with `--skip-scrape`.
3. **Build and categorize:** turns results into a table, removes duplicates, and assigns each reel a category from caption and hashtag keywords. Saved as CSV.
4. **Generate roadmap:** groups reels by category and writes `visual_roadmap.md` with a Mermaid flowchart and a table per category.

`config.py` and `paths.py` provide shared settings and file locations to every step.
