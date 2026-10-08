import json
import os
import sys
from apify_client import ApifyClient
from dotenv import load_dotenv
try:
    from .config import Paths, ACTOR_ID, BATCH_SIZE, DEFAULT_ENCODING
except ImportError:
    from config import Paths, ACTOR_ID, BATCH_SIZE, DEFAULT_ENCODING


class InstagramScraper:
    def __init__(self, api_token: str = None):
        
        if api_token is None:
            load_dotenv()
            api_token = os.getenv("APIFY_API_TOKEN")
            
            if not api_token or api_token.startswith("your_"):
                raise ValueError(
                    "Missing APIFY_API_TOKEN. "
                    "Create .env with: APIFY_API_TOKEN=your_actual_token"
                )
        
        self.token = api_token
        self.client = ApifyClient(api_token)

    def scrape_urls(self, urls: list[str]) -> list[dict]:
        items = []  

        for i in range(0, len(urls), BATCH_SIZE):
            batch = urls[i:i + BATCH_SIZE]
            # urls[0:50] = first 50 items
            # urls[50:100] = next 50 items

            batch_num = i // BATCH_SIZE + 1
            # e        0 // 50 = 0 → batch 1
            #          50 // 50 = 1 → batch 2
            #          100 // 50 = 2 → batch 3

            print(
                f"  Scraping batch {batch_num} "
                f"({len(batch)} URLs)..."
            )

            try:
                # Try to scrape this batch
                batch_items = self._scrape_batch(batch)
                
                # If successful, add to our collection
                items.extend(batch_items)

            except Exception as e:
                # If this batch fails, don't crash
                print(
                    f"Batch {batch_num} failed: {e}",
                    file=sys.stderr
                )
                # Continue to the next batch

        return items

    def _scrape_batch(self, urls: list[str]) -> list[dict]:

        run_input = {
            "directUrls": urls,
            # The URLs to scrape
            
            "resultsType": "posts",
            # We want post data (not stories or other types)
            
            "resultsLimit": 1,
            # Each URL should give 1 result
            # (not multiple results per URL)
            
            "addParentData": False,
            # Don't include profile/user data
            # We only want post data
        }

        run = self.client.actor(ACTOR_ID).call(run_input=run_input)
 
        # Behind the scenes:
        #   - Apify opens a browser
        #   - Goes to each URL
        #   - Extracts data
        #   - Stores in a dataset


#isinstance() checks whether a value is a particular type.
        if isinstance(run, dict):
            # If it's a dictionary
            dataset_id = run["defaultDatasetId"]
        else:
            # If it's an object
            dataset_id = (
                getattr(run, "default_dataset_id", None)
                or run.defaultDatasetId
            )

        batch_items = list(
            self.client.dataset(dataset_id).iterate_items()
        )


        return batch_items

    @staticmethod
    def load_cached() -> list[dict]:

        if not Paths.RAW_CACHE.exists():
            raise FileNotFoundError(
                f"No cached results found at {Paths.RAW_CACHE}. "
                "Run scraper without --skip-scrape first."
            )

        print(f"Using cached results: {Paths.RAW_CACHE}")
        
        cache_content = Paths.RAW_CACHE.read_text(
            encoding=DEFAULT_ENCODING
        )
        
        return json.loads(cache_content)

    def save_cache(self, items: list[dict]) -> None:

        Paths.RAW_CACHE.write_text(
            json.dumps(
                items,
                ensure_ascii=False,  
                indent=2             
            ),
            encoding=DEFAULT_ENCODING
        )
        print(f"Cached results: {Paths.RAW_CACHE}")