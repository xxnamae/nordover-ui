#!/usr/bin/env python3
"""
Script to batch push files to GitHub using mcp__github__push_files tool.
Organizes files into logical batches to stay under parameter size limits.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Tuple

BASE_DIR = Path("/home/user/nordover-ui")
OWNER = "xxnamae"
REPO = "nordover-ui"
BRANCH = "main"
COMMIT_MESSAGE = "docs: migrate framework specifications, decisions, and patterns"


def read_file_content(file_path: Path) -> str:
    """Read file content, handling text files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def collect_files_by_category() -> Dict[str, List[Tuple[Path, str]]]:
    """Collect files organized by category."""
    files_by_category = {
        "root": [],
        "topics": [],
        "decisions": [],
        "other": [],
    }

    # Root files
    root_files = ["CLAUDE.md", "LICENSE", "README.md", "EXECUTION_REFERENCE.md", "PUSH_GUIDE.md", "BATCH_PUSH_INDEX.md"]
    for filename in root_files:
        file_path = BASE_DIR / filename
        if file_path.exists():
            content = read_file_content(file_path)
            rel_path = filename
            files_by_category["root"].append((file_path, rel_path, content))

    # Topics files (docs/wiki/topics/nordover-*.md)
    topics_dir = BASE_DIR / "docs" / "wiki" / "topics"
    if topics_dir.exists():
        for file_path in sorted(topics_dir.glob("nordover-*.md")):
            content = read_file_content(file_path)
            rel_path = str(file_path.relative_to(BASE_DIR))
            files_by_category["topics"].append((file_path, rel_path, content))

    # Decisions files (docs/wiki/decisions/*.md)
    decisions_dir = BASE_DIR / "docs" / "wiki" / "decisions"
    if decisions_dir.exists():
        for file_path in sorted(decisions_dir.glob("*.md")):
            content = read_file_content(file_path)
            rel_path = str(file_path.relative_to(BASE_DIR))
            files_by_category["decisions"].append((file_path, rel_path, content))

    # Other documentation files
    for root, dirs, files in os.walk(BASE_DIR / "docs"):
        # Skip already processed directories
        dirs[:] = [d for d in dirs if not (d == "topics" or d == "decisions")]

        for filename in files:
            if filename.endswith(".md"):
                file_path = Path(root) / filename
                content = read_file_content(file_path)
                rel_path = str(file_path.relative_to(BASE_DIR))
                files_by_category["other"].append((file_path, rel_path, content))

    return files_by_category


def estimate_json_size(files: List[Tuple[Path, str, str]]) -> int:
    """Estimate JSON size for a batch of files."""
    # Rough estimate: file path + content size
    total = 0
    for _, rel_path, content in files:
        total += len(rel_path) + len(content) + 100  # Add overhead for JSON structure
    return total


def create_batches(files_by_category: Dict[str, List[Tuple[Path, str, str]]]) -> List[List[Tuple[str, str]]]:
    """Create batches of files, each batch staying under size limits."""
    MAX_BATCH_SIZE = 8_000_000  # 8MB - conservative limit
    MAX_FILES_PER_BATCH = 10

    batches = []

    # Process in logical order: root, topics, decisions, other
    all_files = (
        files_by_category["root"] +
        files_by_category["topics"] +
        files_by_category["decisions"] +
        files_by_category["other"]
    )

    current_batch = []
    current_size = 0

    for file_path, rel_path, content in all_files:
        file_size = len(rel_path) + len(content) + 100

        # Check if we need to start a new batch
        if (current_batch and
            (current_size + file_size > MAX_BATCH_SIZE or
             len(current_batch) >= MAX_FILES_PER_BATCH)):
            batches.append(current_batch)
            current_batch = []
            current_size = 0

        current_batch.append((rel_path, content))
        current_size += file_size

    # Add the last batch
    if current_batch:
        batches.append(current_batch)

    return batches


def format_batch_as_tool_call(batch_num: int, files: List[Tuple[str, str]]) -> Dict:
    """Format a batch as a tool call parameter."""
    file_objects = [
        {
            "path": path,
            "content": content
        }
        for path, content in files
    ]

    return {
        "owner": OWNER,
        "repo": REPO,
        "branch": BRANCH,
        "files": file_objects,
        "message": COMMIT_MESSAGE
    }


def main():
    """Main execution."""
    print("=" * 80)
    print("GITHUB BATCH PUSH GENERATOR")
    print("=" * 80)
    print()

    # Collect files
    print("Collecting files...")
    files_by_category = collect_files_by_category()

    total_files = sum(len(files) for files in files_by_category.values())
    print(f"Found {total_files} files:")
    for category, files in files_by_category.items():
        print(f"  - {category}: {len(files)} files")
    print()

    # Create batches
    print("Creating batches...")
    batches = create_batches(files_by_category)
    print(f"Created {len(batches)} batches")
    print()

    # Output tool calls
    print("=" * 80)
    print("MCP TOOL CALL PARAMETERS")
    print("=" * 80)
    print()

    for batch_num, batch in enumerate(batches, 1):
        tool_call = format_batch_as_tool_call(batch_num, batch)

        print(f"BATCH {batch_num} ({len(batch)} files)")
        print("-" * 80)
        print()
        print("Tool: mcp__github__push_files")
        print()
        print("Parameters (as JSON):")
        print(json.dumps(tool_call, indent=2))
        print()
        print("Files in this batch:")
        for path, _ in batch:
            print(f"  - {path}")
        print()
        print()

    print("=" * 80)
    print(f"Summary: {len(batches)} batches, {total_files} total files")
    print("=" * 80)


if __name__ == "__main__":
    main()
