import re
import pandas as pd 
from config import CATEGORIES, DEFAULT_CATEGORY
from utils import extract_hashtags

def categorize(caption : str , hashtags : str)-> str:
    text = f"{caption} {hashtags}".lower()

    words = set(re.findall(r"[a-z0-9]+", text))

    best_category = DEFAULT_CATEGORY
    best_score = 0 

    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword in words)

        if score > best_score:
            best_category = category
            best_score = score

    return best_category

def to_dataframe(items: list[dict]) -> pd.DataFrame:
    rows = []

    for item in items:
        caption = item.get("caption") or ""
        hashtags = item.get("hashtags") or extract_hashtags(caption)

        row = {
            "url": item.get("url") or "",
            "shortcode": item.get("shortCode") or "",
            "creator": item.get("ownerUsername") or "",
            "creator_name": item.get("ownerFullName") or "",
            "caption": caption,
            "hashtags": ", ".join(hashtags),
            "likes": item.get("likesCount"),
            "comments": item.get("commentsCount"),
            "views": (
                item.get("videoViewCount")
                or item.get("videoPlayCount")
            ),
            "duration_sec": item.get("videoDuration"),
            "posted_at": item.get("timestamp"),
            "type": (
                item.get("productType")
                or item.get("type")
                or ""
            ),
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    df = df.drop_duplicates(
        subset="url"
    ).reset_index(drop=True)

    df["category"] = df.apply(
        lambda row: categorize(
            row["caption"],
            row["hashtags"]
        ),
        axis=1
    )

    return df