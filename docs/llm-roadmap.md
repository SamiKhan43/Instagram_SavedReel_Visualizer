# Using an LLM for a smarter roadmap

[Back to README](../README.md)

The built-in roadmap uses keyword matching, so some reels land in the wrong group. For better results, give the CSV to an LLM such as Claude, ChatGPT or Gemini and paste the prompt below.

1. Run `python project/main.py` to create `project/data/outputs/saved_reels_enriched_data.csv`.
2. Attach the CSV to your chat. If it is too large, paste only the `url`, `creator`, `caption` and `hashtags` columns, in batches of 30 to 40 reels.
3. Paste this prompt:

````text
I'm attaching a CSV of Instagram Reels I saved (columns: url, shortcode, creator, caption, hashtags, likes, comments, views, category).
Turn it into an interactive visual learning roadmap.

Follow these steps:

1. FILTER
   Keep only reels with educational value (tutorials, roadmaps, courses, resource lists, project ideas, study notes, career advice).
   Remove entertainment, memes, gaming, food, movies, news and anything with no learning content.
   Tell me how many reels you removed and why.

2. GROUP
   Sort the remaining reels into learning tracks by topic
   (for example: Frontend, Backend, Data & SQL, AI & ML, Git & DevOps, CS Fundamentals, Career, Math).
   Ignore the existing "category" column if it looks wrong, and decide from the caption and hashtags.

3. ORDER
   Inside each track, arrange reels into stages from beginner to advanced
   (for example: Foundations -> Core -> Build -> Advanced).
   Order the tracks themselves into a suggested learning path.

4. SUMMARIZE EACH REEL
   Give each reel a short label (under 8 words) based on its caption.
   If the caption lists steps or resources, include them.
   If the caption only says "comment X for the link", say that the actual links are not in the data. Do not invent them.

5. VISUALIZE
   Build an interactive page (HTML) with:
   - one tab per track
   - stages shown as a connected path from start to finish
   - each reel as a clickable card linking to its original URL, with the creator's handle
   - a note at the bottom listing what was left out

Rules:
- Use only information in the CSV. Do not make up content, links or resources.
- Tell me about any reel with an empty caption or missing data instead of guessing.
- If you think a reel is in the wrong track, say so and explain why.
````

**Variations**
- For GitHub flowcharts instead of a web page, replace step 5 with: "Output one Mermaid flowchart per track, in a code block I can paste into GitHub."
- After the first result, try follow-ups such as "move all React reels into a separate track" or "make a 30-day study plan from this".
