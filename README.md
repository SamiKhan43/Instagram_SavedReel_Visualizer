# ReelRoadmap

Turn the educational Reels you saved on Instagram into a CSV and a visual learning roadmap.

```
saved_posts.json -> parse URLs -> Apify enrichment -> CSV -> Mermaid roadmap (Markdown)
```

## The Problem

Most people save far more Reels than they ever revisit. Developers, students and self-learners save tutorials, roadmaps, resource lists and step-by-step guides, planning to study them later. Over time, hundreds of saved posts pile up in one long, unorganized list with no topics, no order and no search.

Getting that knowledge out of Instagram is surprisingly hard:

- **The data export is nearly empty.** `saved_posts.json` contains only raw links. It has no captions, hashtags, creator details or engagement numbers for the posts you saved.
- **LLMs can't read the links.** Instagram requires a login and blocks automated access, so an AI assistant that is given these URLs sees nothing useful.
- **The useful part is in the captions.** Many educational reels put their value in numbered steps, resource lists and roadmaps written in the caption. That text is exactly what the export leaves out.
- **Saved content has no structure.** Even with the text, a flat list doesn't show what to learn first, how topics connect, or which saves cover the same subject.

## The Solution

ReelRoadmap closes the gap in four steps:

1. **Parse** your official `saved_posts.json` export and extract every unique reel URL.
2. **Enrich** each URL through the Apify Instagram scraper, which retrieves the public caption, creator and engagement data that the export leaves out.
3. **Organize** the results into a CSV and group reels by topic.
4. **Visualize** the steps found in captions as Mermaid flowcharts that render directly on GitHub.

**Who it's for:** learners and developers who save educational content on Instagram and want to turn it into an organized study plan.

## Features

- Finds every unique reel/post URL in your export, even if Meta changes the JSON layout.
- Fetches captions, creator, likes, comments, views, duration and post date through `apify/instagram-scraper`.
- Extracts hashtags from the caption text itself, because the scraper's own hashtag field was unreliable.
- Cleans engagement numbers (hidden counts of `-1` become empty cells).
- Groups reels by topic with keyword matching, and detects steps (numbered lists, bullets, arrows) for the flowcharts.
- Caches Apify results so you can re-run the processing for free.

## Project structure

```
 Saved Reels Visualizer
├── .env.example          # template for your Apify token
├── .gitignore
├── README.md
├── requirements.txt
├── docs/                 # detailed guides
└── project/
    ├── main.py           # entry point
    ├── cli.py            # arguments and the 4-step pipeline
    ├── config.py         # re-exports constants and paths
    ├── constants.py      # patterns, categories, irrelevant phrases, settings
    ├── paths.py          # every file and folder location
    ├── scraper.py        # Apify calls, batching, cache
    ├── processor.py      # raw results -> clean table (CSV)
    ├── visualization.py  # table -> Mermaid roadmap (Markdown)
    ├── utils.py          # URL parsing and text helpers
    └── data/             # private, git-ignored
        ├── saved_posts.json        (you add this)
        └── outputs/
            ├── apify_raw_results.json
            ├── saved_reels_enriched_data.csv
            └── visual_roadmap.md
```

## Quick start

```bash
python3 -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                # add your Apify token
# copy your saved_posts.json into project/data/
python project/main.py --limit 5                    # small test run
```

Outputs appear in `project/data/outputs/`. See [Setup](docs/setup.md) for the full walkthrough.

## Documentation

| Guide | What's inside |
|---|---|
| [Setup](docs/setup.md) | Requirements, virtual environment, Apify token, exporting your Instagram data |
| [Usage and outputs](docs/usage.md) | Commands, flags, CSV columns, viewing the Mermaid roadmap |
| [How it works](docs/how-it-works.md) | Each module and what it does, and how to customize topics |
| [LLM roadmap prompt](docs/llm-roadmap.md) | A ready-to-paste prompt for a smarter, interactive roadmap |
| [Troubleshooting and limitations](docs/troubleshooting.md) | Common errors and what the tool can't do |
| [Privacy and responsible use](docs/privacy.md) | Keeping your data and token safe |

## Privacy

`.env` and `project/data/` are git-ignored. Your saved posts reveal personal interests, so keep any repo with outputs private. Details in [Privacy and responsible use](docs/privacy.md).

## License


 Saved Reels Visualizer  is licensed under the MIT License.