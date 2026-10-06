import argparse
import os
import sys
import re
import json
from collections import OrderedDict
from pathlib import Path

import pandas as pd
from apify_client import ApifyClient
from dotenv import load_dotenv

ROOT = Path(__file__).parent #__file__ is a special python variable that contain the path of the current python file 
DATA_DIR = ROOT / "data" #means add data dir in our current dir
OUT_DIR = DATA_DIR / "Outputs" #same logic as data dir
INPUT_FILE = DATA_DIR / "saved_posts.json"
RAW_CACHE = OUT_DIR / "apify_raw_results.json"
CSV_FILE = OUT_DIR / "saved_reels_enriched_data.csv"
MD_FILE = OUT_DIR / "visual_roadmap.md"

#in appify an actor is basically a tool that perform specific tasks like Instagram scraping
ACTOR_ID = "apify/instagram-scraper"
BATCH_SIZE = 50 #program will process 50 items at a time
