import re
from config import (
    CLEAN_LABEL_MAX_LEN,
    STEP_LINE_PATTERN,
    MAX_STEPS_PER_REEL,
    HASHTAG_PATTERN,
    CATEGORIES,
    DEFAULT_CATEGORY,
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
        elif "→" in line or "->" in line:
            steps.extend(re.split(r"→|->", line)) 

    steps = [clean_label(s) for s in steps]
    steps = [s for s in steps if len(s) > 2]

    if not steps:
        lines = [clean_label(line) for line in caption.splitlines()]
        steps = [line for line in lines if len(line) > 3][:3]

    return steps[:max_steps]

def safe_int(value, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError , OverflowError):
        return default


