from paths import Paths
from constants import (
    ACTOR_ID,
    BATCH_SIZE,
    INSTAGRAM_URL_PATTERN,
    STEP_LINE_PATTERN,
    CATEGORIES,
    DEFAULT_CATEGORY,
    CLEAN_LABEL_MAX_LEN,
    MAX_STEPS_PER_REEL,
    DEFAULT_ENCODING,
    CSV_ENCODING,
    HASHTAG_PATTERN,
    IRRELEVANT_PHRASES
)

# Whenever any program need to import constants and path.it can use this central config file
# Re-export everything so modules can do:
# from config import Paths, BATCH_SIZE, etc.
__all__ = [
    "Paths",
    "ACTOR_ID",
    "BATCH_SIZE",
    "INSTAGRAM_URL_PATTERN",
    "STEP_LINE_PATTERN",
    "CATEGORIES",
    "DEFAULT_CATEGORY",
    "CLEAN_LABEL_MAX_LEN",
    "MAX_STEPS_PER_REEL",
    "DEFAULT_ENCODING",
    "CSV_ENCODING",
    "HASHTAG_PATTERN",
    "IRRELEVANT_PHRASES"
]
