# How it works

[Back to README](../README.md)

## The pipeline

`main.py` parses the command-line flags and calls `run()` in `cli.py`, which runs four steps:

1. **Parse** (`utils.extract_reel_urls`). Walks the whole JSON, because the export layout changes between versions, and collects every unique Instagram reel/post URL.
2. **Enrich** (`scraper.InstagramScraper`). Sends URLs to `apify/instagram-scraper` in batches of 50. A failed batch is reported but does not stop the run. Results are cached to `apify_raw_results.json`. The code works with both old and new versions of `apify-client`.
3. **Process** (`processor.to_dataframe`). Builds the pandas table: hashtags are extracted from the caption, counts are cleaned, failed rows are skipped, and `categorize()` assigns a topic by counting keyword matches.
4. **Visualize** (`visualization.write_markdown`). Detects steps in each caption and writes one Mermaid flowchart per topic, which keeps each chart under GitHub's size limit.

## Modules

| File | Responsibility |
|---|---|
| `constants.py` | Fixed values: actor name, batch size, regex patterns, categories, irrelevant phrases |
| `config.py` | One place to import constants and paths from |
| `paths.py` | Where every file and folder lives (`Paths` class) |
| `utils.py` | `extract_reel_urls`, `clean_label`, `extract_hashtags`, `extract_steps`, `is_irrelevant`, `safe_int` |
| `scraper.py` | Apify client, batching, cache read/write |
| `processor.py` | `categorize`, `to_dataframe` |
| `visualization.py` | `build_mermaid`, `write_markdown` |
| `cli.py` | Flags and the pipeline |
| `main.py` | Entry point |

## Customizing

All settings live in `project/constants.py`:

- **Topics:** edit the `CATEGORIES` dictionary to add or change keyword groups.
- **Irrelevant lines:** `IRRELEVANT_PHRASES` lists call-to-action phrases ("follow @", "link in bio") that are skipped when picking steps. Keep the phrases specific, because a short one like "dm" would also match words such as "admin".
- **Batch size:** change `BATCH_SIZE` if you hit Apify limits.
- **Chart size:** `MAX_STEPS_PER_REEL` and `CLEAN_LABEL_MAX_LEN` control how much of each caption appears in the flowchart.