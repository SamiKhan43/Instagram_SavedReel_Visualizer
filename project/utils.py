import re
import json
from pathlib import Path
try:
    from .config import (
        CLEAN_LABEL_MAX_LEN,
        STEP_LINE_PATTERN,
        MAX_STEPS_PER_REEL,
        HASHTAG_PATTERN,
        CATEGORIES,
        DEFAULT_CATEGORY,
        IRRELEVANT_PHRASES,
        DEFAULT_ENCODING,
        INSTAGRAM_URL_PATTERN
    )
except ImportError:
    from config import (
        CLEAN_LABEL_MAX_LEN,
        STEP_LINE_PATTERN,
        MAX_STEPS_PER_REEL,
        HASHTAG_PATTERN,
        CATEGORIES,
        DEFAULT_CATEGORY,
        IRRELEVANT_PHRASES,
        DEFAULT_ENCODING,
        INSTAGRAM_URL_PATTERN
    )

STEP_RE = re.compile(STEP_LINE_PATTERN, re.IGNORECASE)

def clean_label(text : str , max_len : int = CLEAN_LABEL_MAX_LEN):
    #  This function:
    # - Removes URLs
    # - Removes hashtags and mentions
    # - Removes special characters
    # - Limits length to fit in Mermaid nodes

    #re.sub(pattern, relacement, text)
    #what to find,  what to put instead,  where to look
    text = text or ""
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[#@]\w+", "", text)
    text = re.sub(r"""["'`<>{}\[\]()|;\\]""", "", text)
    text = re.sub(r"[^\w\s\-\.,:&/+!?%]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_len:
        return text[:max_len].rstrip() + "…"
    return text

#Extract hashtags from text
def extract_hashtags(text : str) -> list[str]:
    text = text or ""
    tags = re.findall(HASHTAG_PATTERN , text)
    tags = [tag.lower() for tag in tags]
    return list(dict.fromkeys(tags))

def extract_steps(caption:str , max_steps : int = MAX_STEPS_PER_REEL ) -> list[str]:
    caption = caption or ""
    steps = []

    for line in caption.splitlines():
        m = STEP_RE.match(line)
        if m:
            steps.append(m.group(1))
        elif ("→" in line or "->" in line) and not is_irrelevant(line):
            steps.extend(re.split(r"→|->", line)) 

    steps = [clean_label(s) for s in steps]
    steps = [s for s in steps if len(s) > 2]

    if not steps:
        lines = [clean_label(line) for line in caption.splitlines() if not is_irrelevant(line)]
        steps = [line for line in lines if len(line) > 3][:3]

    return steps[:max_steps]

def is_irrelevant(line: str) -> bool: #return true as soon as one irrelevant phrases appears inside a line
    line = line.lower()
    return any(phrase in line for phrase in IRRELEVANT_PHRASES)

def safe_int(value, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError , OverflowError):
        return default

def extract_reel_urls(path: Path) -> list[str]:
    with open(path, "r", encoding=DEFAULT_ENCODING) as f:
        data = json.load(f)

    found = {}
    pattern = re.compile(INSTAGRAM_URL_PATTERN)

    def walk(node):
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            for match in pattern.findall(node):
                found[match.rstrip("/") + "/"] = None

    walk(data)
    return list(found.keys())
