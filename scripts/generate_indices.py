from pathlib import Path
import re

DOCS_DIR = Path("docs")

EXCLUDE_FILES = {"README.md", "index.md"}


def title_from_folder(folder_name):
    return " ".join(word.capitalize() for word in folder_name.split("-"))


def extract_title(md_file):
    text = md_file.read_text(encoding="utf-8")

    # Prefer YAML front matter title
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', text, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Fallback to first Markdown heading
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Final fallback: filename
    return md_file.stem.replace("-", " ").title()


def generate_readme(topic_dir):
    topic_title = title_from_folder(topic_dir.name)

    qa_files = [
        f for f in topic_dir.glob("*.md")
        if f.name not in EXCLUDE_FILES
    ]

    qa_items = sorted(
        [(extract_title(f), f.name) for f in qa_files],
        key=lambda x: x[0].lower()
    )

    lines = [f"# {topic_title}", ""]

    if not qa_items:
        lines.append("_No questions have been added yet._")
        lines.append("")
    else:
        lines.append("Questions in this section:")
        lines.append("")

        for i, (title, filename) in enumerate(qa_items, start=1):
            lines.append(f"{i}. [{title}]({filename})")
            lines.append("")

    readme_path = topic_dir / "README.md"
    readme_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Updated {readme_path}")


def main():
    for item in sorted(DOCS_DIR.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            generate_readme(item)


if __name__ == "__main__":
    main()
