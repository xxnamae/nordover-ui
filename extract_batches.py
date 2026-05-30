#!/usr/bin/env python3
"""
Extract just the batch parameters as executable Python code.
"""

import os
import json
from pathlib import Path

BASE_DIR = Path("/home/user/nordover-ui")
OWNER = "xxnamae"
REPO = "nordover-ui"
BRANCH = "main"
COMMIT_MESSAGE = "docs: migrate framework specifications, decisions, and patterns"


def read_file_content(file_path: Path) -> str:
    """Read file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return ""


def collect_and_batch_files():
    """Collect files and create batches."""
    MAX_BATCH_SIZE = 8_000_000
    MAX_FILES_PER_BATCH = 10

    files = []

    # Root files (in order)
    root_files = ["CLAUDE.md", "LICENSE", "README.md", "EXECUTION_REFERENCE.md", "PUSH_GUIDE.md", "BATCH_PUSH_INDEX.md"]
    for filename in root_files:
        file_path = BASE_DIR / filename
        if file_path.exists():
            content = read_file_content(file_path)
            files.append((filename, content))

    # Topics (nordover-*.md)
    topics_dir = BASE_DIR / "docs" / "wiki" / "topics"
    if topics_dir.exists():
        for file_path in sorted(topics_dir.glob("nordover-*.md")):
            content = read_file_content(file_path)
            rel_path = str(file_path.relative_to(BASE_DIR))
            files.append((rel_path, content))

    # Decisions
    decisions_dir = BASE_DIR / "docs" / "wiki" / "decisions"
    if decisions_dir.exists():
        for file_path in sorted(decisions_dir.glob("*.md")):
            content = read_file_content(file_path)
            rel_path = str(file_path.relative_to(BASE_DIR))
            files.append((rel_path, content))

    # Other docs
    for root, dirs, filenames in os.walk(BASE_DIR / "docs"):
        dirs[:] = [d for d in dirs if d not in ("topics", "decisions")]
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = Path(root) / filename
                content = read_file_content(file_path)
                rel_path = str(file_path.relative_to(BASE_DIR))
                files.append((rel_path, content))

    # Create batches
    batches = []
    current_batch = []
    current_size = 0

    for path, content in files:
        file_size = len(path) + len(content) + 100

        if (current_batch and
            (current_size + file_size > MAX_BATCH_SIZE or
             len(current_batch) >= MAX_FILES_PER_BATCH)):
            batches.append(current_batch)
            current_batch = []
            current_size = 0

        current_batch.append({"path": path, "content": content})
        current_size += file_size

    if current_batch:
        batches.append(current_batch)

    return batches


def main():
    batches = collect_and_batch_files()

    print(f"# Total batches: {len(batches)}")
    print(f"# Total files: {sum(len(b) for b in batches)}\n")

    for i, batch in enumerate(batches, 1):
        print(f"# BATCH {i} ({len(batch)} files)")
        print("batch_{}_params = {{".format(i))
        print('    "owner": "{}",'.format(OWNER))
        print('    "repo": "{}",'.format(REPO))
        print('    "branch": "{}",'.format(BRANCH))
        print('    "files": [')

        for j, file_obj in enumerate(batch):
            print('        {')
            print('            "path": {},'.format(json.dumps(file_obj["path"])))
            print('            "content": {},'.format(json.dumps(file_obj["content"])))
            print('        }' + (',' if j < len(batch) - 1 else ''))

        print('    ],')
        print('    "message": {}'.format(json.dumps(COMMIT_MESSAGE)))
        print("}")
        print()


if __name__ == "__main__":
    main()
