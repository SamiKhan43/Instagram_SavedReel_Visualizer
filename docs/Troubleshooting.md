# Troubleshooting and limitations

[Back to README](../README.md)

## Troubleshooting

| Problem | Fix |
|---|---|
| `Cannot connect to the Docker daemon` | Docker is not running. Start Docker Desktop, or on Linux run `sudo systemctl start docker`. |
| `Missing APIFY_API_TOKEN` | `.env` is missing, misnamed (it must be exactly `.env`), still has the placeholder, or you ran the command from a folder other than the repo root. |
| `ModuleNotFoundError: dotenv` or `apify_client` | The image is out of date. Run `docker compose build` again. |
| `Put your Instagram export at ...` | `saved_posts.json` is not in the `data/` folder in the repo root (Docker mounts it as `/app/data`). |
| `'Run' object is not subscriptable` | You have an old `scraper.py` and a newer `apify-client`. The current `_scrape_batch` handles both. |
| `Apify returned no data` | Check your Apify credits and that the reels are public. |
| Log says `Crawled 57/58 pages` | Not an error. If the status is `SUCCEEDED` and failed requests are 0, the run worked. |
| Fewer rows in the CSV than URLs found | Private, deleted or restricted posts are skipped. This is normal. |
| Code changes have no effect | The image still holds the old code. Run `docker compose build`. |
| Files in `data/outputs/` are owned by root (Linux) | Run `sudo chown -R $USER data`. |
| `UnicodeEncodeError` in the terminal | Remove emoji from `print` messages (some Windows terminals can't show them). |
| Roadmap only shows text | Your Markdown viewer does not support Mermaid. See [Usage](usage.md). |

## Limitations

- Only **public** posts can be scraped. Private accounts and removed posts return nothing.
- Many creators write "comment X for the link". Those links are sent by DM, so they are not in the caption data.
- Topic grouping and step detection are keyword-based, so some reels will land in the wrong group or show weak steps. A common improvement is to send each caption to an LLM to classify topics and extract ordered steps (see the [LLM roadmap prompt](llm-roadmap.md)).
- Very large topics can produce a chart too big for GitHub to render. If that happens, split the topic into smaller groups.
- Apify pricing and the scraper's output fields can change. Check the [actor page](https://apify.com/apify/instagram-scraper) if something stops working.