# Privacy and responsible use

[Back to README](../README.md)

- `.gitignore` blocks `.env` and everything in `project/data/`, so your token, your saved list and the outputs are not committed. Run `git status` before every push to confirm. The data folder is inside `project/`, so the ignore rule must point there, as the provided `.gitignore` does.
- If you ever commit a token by mistake, revoke it in the Apify console and create a new one. Deleting the file in a later commit does not remove it from Git history.
- Your saved posts reveal personal interests. Keep any repo containing the outputs private, or only publish a small sample.
- Only collect public data, follow Instagram's and Apify's terms of service, and respect creators' rights. This project is for organizing your own learning.