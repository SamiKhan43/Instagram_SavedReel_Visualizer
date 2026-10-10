# ReelRoadmap

Turn the educational Reels you save on Instagram into a CSV and a visual learning roadmap.

```text
saved_posts.json → Extract URLs → Apify enrichment → CSV → Mermaid roadmap
```

## The Problem

People save hundreds of Instagram Reels to revisit later, but those saves often become an unorganized collection of links.

Educational Reels contain tutorials, learning roadmaps, resource lists, and step-by-step guides. Unfortunately, Instagram's saved-posts export doesn't provide all the information needed to organize this content effectively.

- **Limited export data:** `saved_posts.json` primarily contains saved-post links, not the captions and metadata needed to organize educational content.
- **Limited access to captions:** Instagram restricts automated access, making it difficult for external tools to retrieve information from saved Reels.
- **Valuable information in captions:** Tutorials and roadmaps often contain their most useful information in captions.
- **No learning structure:** A flat list of saved posts doesn't show related topics or the steps involved in learning a subject.

## The Solution

ReelRoadmap transforms your saved Instagram content into an organized learning resource through four steps:

1. **Extract:** Parse your official `saved_posts.json` export and find unique Reel URLs.
2. **Enrich:** Use the Apify Instagram scraper to retrieve available captions, creator information, and engagement data.
3. **Organize:** Clean the collected data, categorize Reels by topic, and export the results to CSV.
4. **Visualize:** Identify steps in captions and generate Mermaid flowcharts in Markdown.

**Who is it for?**

Students, developers, and self-learners who save educational Instagram Reels and want to organize them into a more useful learning resource.

## Features

- Extracts unique Instagram Reel URLs from nested export JSON.
- Retrieves available captions and post metadata through `apify/instagram-scraper`.
- Collects available creator, engagement, duration, and publication information.
- Extracts hashtags directly from caption text.
- Cleans engagement values, including hidden counts represented by `-1`.
- Categorizes Reels using keyword matching.
- Detects numbered lists, bullets, and arrows that may represent learning steps.
- Caches Apify results to support reprocessing without unnecessary API calls.
- Exports enriched data to CSV.
- Generates Mermaid learning roadmaps in Markdown.
- Supports command-line options for limiting processing and reusing cached results.

**Note:** Scraping results depend on Instagram's accessibility, the Apify actor, and the availability of post data. Not every Reel will necessarily produce complete metadata.

## Project Structure

```text
ReelRoadmap/
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── compose.yaml
├── README.md
├── requirements.txt
├── LICENSE
├── docs/
│   ├── setup.md
│   ├── usage.md
│   ├── how-it-works.md
│   ├── llm-roadmap.md
│   ├── troubleshooting.md
│   └── privacy.md
├── data/
│   ├── saved_posts.json
│   └── Outputs/
│       ├── apify_raw_results.json
│       ├── saved_reels_enriched_data.csv
│       └── visual_roadmap.md
└── project/
    ├── main.py
    ├── cli.py
    ├── config.py
    ├── constants.py
    ├── paths.py
    ├── scraper.py
    ├── processor.py
    ├── visualization.py
    └── utils.py
```

The `data/` directory contains your personal Instagram export and generated files. These files should remain private and should not be committed to a public repository.

## Quick start
 
Requires [Docker](https://docs.docker.com/get-docker/) with Docker Compose. You do not need Python installed.
 
```bash
cp .env.example .env                                # add your Apify token
mkdir -p data                                       # then copy your saved_posts.json into data/
docker compose build
docker compose run --rm reels --limit 5             # small test run
```
 
Outputs appear in `data/outputs/`. See [Setup](docs/setup.md) for the full walkthrough.
 
## Documentation
 
| Guide | What's inside |
|---|---|
| [Setup](docs/setup.md) | Requirements, Docker image, Apify token, exporting your Instagram data |
| [Usage and outputs](docs/usage.md) | Commands, flags, CSV columns, viewing the Mermaid roadmap |
| [How it works](docs/how-it-works.md) | Each module and what it does, and how to customize topics |
| [LLM roadmap prompt](docs/llm-roadmap.md) | A ready-to-paste prompt for a smarter, interactive roadmap |
| [Troubleshooting and limitations](docs/troubleshooting.md) | Common errors and what the tool can't do |
| [Privacy and responsible use](docs/privacy.md) | Keeping your data and token safe |
 
## Privacy
 
`.env` and `project/data/` are git-ignored. Your saved posts reveal personal interests, so keep any repo with outputs private. Details in [Privacy and responsible use](docs/privacy.md).
 

## License

ReelRoadmap is licensed under the MIT License. See [LICENSE](LICENSE) for details.