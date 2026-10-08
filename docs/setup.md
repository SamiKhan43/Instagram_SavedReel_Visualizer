# Setup

[Back to README](../README.md)

## Requirements

- Python 3.9 or newer
- An [Apify account](https://console.apify.com) and API token (the free plan includes some monthly credit)
- Your Instagram data export in JSON format

## 1. Get the code

```bash
git clone <your-repo-url>
cd reelroadmap
```

## 2. Create a virtual environment and install packages

A virtual environment is required on many Linux and Mac systems. Without it, pip may fail with an `externally-managed-environment` error.

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Your prompt should start with `(venv)`. Run the activate command again every time you open a new terminal. On Ubuntu/Debian, if `venv` fails, run `sudo apt install python3-venv` first.

## 3. Add your Apify token

```bash
cp .env.example .env            # Windows: copy .env.example .env
```

Open `.env` in the repo root and replace the placeholder, with no quotes:

```
APIFY_API_TOKEN=apify_api_xxxxxxxxxxxxxxxx
```

Find your token in the Apify console under **Settings > Integrations**. Never commit this file or share the token.

## 4. Export your Instagram data

1. In Instagram, go to **Accounts Center > Your information and permissions > Download your information**.
2. Choose **JSON** as the format and make sure **Saved** content is included. (Menu names change over time, so look for the closest equivalent.)
3. When the export is ready, download it and find `saved_posts.json` (usually inside a `your_instagram_activity/saved/` folder).
4. Copy it into `project/data/`. The folder is created automatically the first time you run the program.