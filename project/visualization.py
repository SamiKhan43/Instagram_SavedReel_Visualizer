import pandas as pd

from config import Paths
from utils import clean_label, extract_steps, safe_int

def build_mermaid(df: pd.DataFrame) -> str:
    lines = [
        "flowchart TD",
        '  ROOT(["My Learning Roadmap"])'
    ]

    for category_index, (category, group) in enumerate(
        df.groupby("category", sort=False)
    ):
        category_id = f"C{category_index}"

        lines.append(
            f'  subgraph {category_id}_sg'
            f'["{clean_label(category, 40)}"]'
        )
        lines.append("    direction TB")

        for reel_index, row in enumerate(group.itertuples()):
            reel_id = f"{category_id}R{reel_index}"

            title = (
                clean_label(row.caption.splitlines()[0], 40)
                if row.caption
                else row.shortcode
            ) or row.shortcode

            lines.append(
                f'    {reel_id}["{title}'
                f'<br/>@{clean_label(row.creator, 25)}"]'
            )

            previous_id = reel_id

            for step_index, step in enumerate(extract_steps(row.caption)):
                step_id = f"{reel_id}S{step_index}"

                lines.append(f'    {step_id}("{step}")')
                lines.append(f"    {previous_id} --> {step_id}")

                previous_id = step_id

        lines.append("  end")
        lines.append(f"  ROOT --> {category_id}_sg")

    return "\n".join(lines)

def write_markdown(df: pd.DataFrame) -> None:
    parts = [
        "# Visual Learning Roadmap",
        "",
        f"Generated from **{len(df)}** saved reels.",
        ""
    ]

    for category, group in df.groupby("category", sort=False):
        parts.extend([
            f"## {category} ({len(group)})",
            "",
            "```mermaid",
            build_mermaid(group),
            "```",
            "",
            "| Creator | Reel | Likes |",
            "|---|---|---|"
        ])

        for row in group.itertuples():
            likes = "" if pd.isna(row.likes) else int(row.likes)

            parts.append(
                f"| @{row.creator} | "
                f"[{row.shortcode}]({row.url}) | "
                f"{likes} |"
            )
        parts.append("")

    Paths.MD_FILE.write_text(
        "\n".join(parts),
        encoding="utf-8"
    )