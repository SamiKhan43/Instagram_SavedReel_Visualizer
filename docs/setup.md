# Setup

[Back to README](../README.md)

## Requirements

- [Docker](https://docs.docker.com/get-docker/) with Docker Compose v2 (Docker Desktop on Windows and Mac, Docker Engine on Linux). Python does not need to be installed on your machine.
- An [Apify account](https://console.apify.com) and API token (the free plan includes some monthly credit)
- Your Instagram data export in JSON format

## 1. Get the code

```bash
git clone <your-repo-url>
cd reelroadmap
```

## 2. Build the Docker image

Check that Docker is running:

```bash
docker --version
docker compose version
```

Then build the image from the repo root:

```bash
docker compose build
```

The first build downloads Python and installs the packages from `requirements.txt`, which takes a minute or two. Run `docker compose build` again whenever you change the code or `requirements.txt`.

## 3. Add your Apify token

```bash
cp .env.example .env            # Windows: copy .env.example .env
```

Open `.env` in the repo root and replace the placeholder, with no quotes:

```
APIFY_API_TOKEN=apify_api_xxxxxxxxxxxxxxxx
```

Find your token in the Apify console under **Settings > Integrations**. Docker Compose reads this file automatically when you run commands from the repo root and passes the token into the container. It is not copied into the image. Never commit this file or share the token.

## 4. Export your Instagram data

1. In Instagram, go to **Accounts Center > Your information and permissions > Download your information**.
2. Choose **JSON** as the format and make sure **Saved** content is included. (Menu names change over time, so look for the closest equivalent.)
3. When the export is ready, download it and find `saved_posts.json` (usually inside a `your_instagram_activity/saved/` folder).
4. Copy it into the `data/` folder in the repo root. Create the folder first (`mkdir -p data`) if it does not exist, because if Docker creates it for you it may be owned by root on Linux.