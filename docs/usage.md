# Usage and outputs

[Back to README](../README.md)

## Run

Run these from the repo root, with Docker running.

Do a small test run first, because Apify charges per result:

```bash
docker compose run --rm reels --limit 5
```

Then run everything:

```bash
docker compose run --rm reels
```

| Flag | What it does |
|---|---|
| `--limit N` | Process only the first N reels (cheap test) |
| `--skip-scrape` | Reuse the cached Apify results and skip Apify, so there is no cost and no token is needed |

If you change the grouping or flowchart logic, run `docker compose build` to pick up the code change, then use `--skip-scrape` to rebuild the outputs instantly:

```bash
docker compose run --rm reels --skip-scrape
```

> Warning: a normal run (without `--skip-scrape`) overwrites the cache. If you do a `--limit 5` test after a full scrape, the cache will contain only 5 results. Run the full scrape last, or back up `apify_raw_results.json` first.

## Outputs

All outputs are written to `data/outputs/` in the repo root (the folder Docker mounts into the container).

**`saved_reels_enriched_data.csv`** has these columns: `url`, `shortcode`, `creator`, `creator_name`, `caption`, `hashtags`, `likes`, `comments`, `views`, `duration_sec`, `posted_at`, `type`, `category`. Open it in Excel or Google Sheets. A cell is empty when the creator hid the number or the post type has none (for example, views on a carousel).

**`visual_roadmap.md`** has one section per topic, each with a Mermaid flowchart and a table of links. It looks like plain text until you open it in a viewer that supports Mermaid:

- **GitHub:** push it to a repo (use a private one) and open the file.
- **VS Code:** install the "Markdown Preview Mermaid Support" extension and press `Ctrl+Shift+V`.
- **Online:** paste one chart block into [mermaid.live](https://mermaid.live).

**`apify_raw_results.json`** is the cache of everything Apify returned.