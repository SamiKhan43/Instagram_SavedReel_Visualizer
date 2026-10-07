ACTOR_ID = "apify/instagram-scraper"
BATCH_SIZE = 50 


#WHY ARE WE USING REGEX?
#Instead of searching for exact words, we use a special syntax to describe the shape of the text we are looking for. 

#it can recognize URL structures
INSTAGRAM_URL_PATTERN = (
    r"https?://(?:www\.)?instagram\.com/(?:reels?|p|tv)/[A-Za-z0-9_\-]+/?"
    )

#it can recognize instagram post captions
STEP_LINE_PATTERN = (
    r"^\s*(?:\d+[\.\)\-:]|"
    r"[0-9]\uFE0F?\u20E3|"
    r"step\s*\d+[:\.\-]?|"
    r"[-•●▪️✅👉➡️→*])\s*(.+)$"
)

HASHTAG_PATTERN = r"#(\w+)"

CATEGORIES = {
    "Python": [
        "python", "pandas", "numpy", "django", "flask", "fastapi"
    ],
    "Web Development": [
        "html", "css", "javascript", "react", "nextjs", "frontend",
        "backend", "webdev", "node", "typescript"
    ],
    "AI & Machine Learning": [
        "ai", "machinelearning", "ml", "llm", "chatgpt", "deeplearning",
        "datascience", "neural", "prompt", "genai"
    ],
    "Data & SQL": [
        "sql", "database", "dataanalysis", "powerbi", "tableau",
        "excel", "analytics"
    ],
    "DevOps & Cloud": [
        "docker", "kubernetes", "aws", "azure", "cloud", "devops",
        "linux", "git", "github"
    ],
    "Career & Interviews": [
        "career", "interview", "resume", "job", "internship",
        "roadmap", "dsa", "leetcode"
    ],
    "Cybersecurity": [
        "cybersecurity", "hacking", "security", "pentest"
    ],
    "Design & Other Skills": [
        "design", "figma", "uiux", "productivity", "freelance"
    ],
}

IRRELEVANT_PHRASES = [
    "follow", "comment", "save this", "share", "link in bio",
    "dm", "tag a friend", "subscribe", "like and",
]

DEFAULT_CATEGORY = "General Learning"
# If a post does not match any category keywords, it gets this

CLEAN_LABEL_MAX_LEN = 45
# Maximum length for Mermaid node labels

MAX_STEPS_PER_REEL = 6
# Maximum number of learning steps to extract from a caption

DEFAULT_ENCODING = "utf-8"
CSV_ENCODING = "utf-8-sig"  
