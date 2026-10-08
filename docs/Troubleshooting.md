# Troubleshooting and limitations

[Back to README](../README.md)

## Troubleshooting

| Problem | Fix |
|---|---|
| `externally-managed-environment` when running pip | Use a virtual environment (see [Setup](setup.md)). Don't use `--break-system-packages`. |
| `Missing APIFY_API_TOKEN` | `.env` is missing, misnamed (it must be exactly `.env`), or still has the placeholder. |
| `ModuleNotFoundError: dotenv` or `apify_client` | The virtual environment is not active, or you skipped `pip install -r requirements.txt`. |
| `Put your Instagram export at ...` | `saved_posts.json` is not in `project/data/`. |
| `'Run' object is not subscriptable` | You have an old `scraper.py` and a newer `apify-client`. The current `_scrape_batch` handles both. |
| `Apify returned no data` | Check your Apify credits and that the reels are public. |
| Log says `Crawled 57/58 pages` | Not an error. If the status is `SUCCEEDED` and failed requests are 0, the run worked. |
| Fewer rows in the CSV than URLs found | Private, deleted or restricted posts are skipped. This is normal. |
| `UnicodeEncodeError` in the terminal | Remove emoji from `print` messages (some Windows terminals can't show them). |
| Roadmap only shows text | Your Markdown viewer does not support Mermaid. See [Usage](usage.md). |

## Limitations

- Only **public** posts can be scraped. Private accounts and removed posts return nothing.
- Many creators write "comment X for the link". Those links are sent by DM, so they are not in the caption data.
- Topic grouping and step detection are keyword-based, so some reels will land in the wrong group or show weak steps. A common improvement is to send each caption to an LLM to classify topics and extract ordered steps (see the [LLM roadmap prompt](llm-roadmap.md)).
- Very large topics can produce a chart too big for GitHub to render. If that happens, split the topic into smaller groups.
- Apify pricing and the scraper's output fields can change. Check the [actor page](https://apify.com/apify/instagram-scraper) if something stops working.