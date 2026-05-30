#!/usr/bin/env python3
"""
Show batch manifest - which files are in each batch.
"""

import os
from pathlib import Path

BASE_DIR = Path("/home/user/nordover-ui")

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except:
        return 0

def collect_files():
    """Collect all files in order."""
    files = []

    # Root files
    root_files = ["CLAUDE.md", "LICENSE", "README.md", "EXECUTION_REFERENCE.md", "PUSH_GUIDE.md", "BATCH_PUSH_INDEX.md"]
    for filename in root_files:
        file_path = BASE_DIR / filename
        if file_path.exists():
            size = get_file_size(file_path)
            files.append((filename, size))

    # Topics (nordover-*.md)
    topics_dir = BASE_DIR / "docs" / "wiki" / "topics"
    if topics_dir.exists():
        for file_path in sorted(topics_dir.glob("nordover-*.md")):
            rel_path = str(file_path.relative_to(BASE_DIR))
            size = get_file_size(file_path)
            files.append((rel_path, size))

    # Decisions
    decisions_dir = BASE_DIR / "docs" / "wiki" / "decisions"
    if decisions_dir.exists():
        for file_path in sorted(decisions_dir.glob("*.md")):
            rel_path = str(file_path.relative_to(BASE_DIR))
            size = get_file_size(file_path)
            files.append((rel_path, size))

    # Other docs
    for root, dirs, filenames in os.walk(BASE_DIR / "docs"):
        dirs[:] = [d for d in dirs if d not in ("topics", "decisions")]
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = Path(root) / filename
                rel_path = str(file_path.relative_to(BASE_DIR))
                size = get_file_size(file_path)
                files.append((rel_path, size))

    return files

def create_batches(files):
    """Create batches."""
    MAX_BATCH_SIZE = 8_000_000
    MAX_FILES_PER_BATCH = 10

    batches = []
    current_batch = []
    current_size = 0

    for path, size in files:
        if (current_batch and
            (current_size + size > MAX_BATCH_SIZE or
             len(current_batch) >= MAX_FILES_PER_BATCH)):
            batches.append(current_batch)
            current_batch = []
            current_size = 0

        current_batch.append((path, size))
        current_size += size

    if current_batch:
        batches.append(current_batch)

    return batches

def format_size(bytes):
    """Format bytes to readable size."""
    for unit in ['B', 'KB', 'MB']:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024
    return f"{bytes:.1f}GB"

def main():
    files = collect_files()
    batches = create_batches(files)

    print("=" * 100)
    print("BATCH MANIFEST")
    print("=" * 100)
    print()
    print(f"Total files: {len(files)}")
    print(f"Total batches: {len(batches)}")
    print()

    total_bytes = 0
    for batch_num, batch in enumerate(batches, 1):
        batch_size = sum(size for _, size in batch)
        total_bytes += batch_size

        print(f"BATCH {batch_num}: {len(batch)} files, {format_size(batch_size)}")
        print("-" * 100)

        for path, size in batch:
            print(f"  {path:<70} {format_size(size):>10}")
        print()

    print("=" * 100)
    print(f"Total size: {format_size(total_bytes)}")
    print("=" * 100)

if __name__ == "__main__":
    main()
