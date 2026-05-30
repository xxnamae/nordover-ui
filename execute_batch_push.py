#!/usr/bin/env python3
"""
Execute the batch push to GitHub.
This script imports batch parameters and shows the tool calls needed.
"""

import json
from pathlib import Path

# Import batch parameters
from BATCH_PARAMETERS import (
    batch_1_params,
    batch_2_params,
    batch_3_params,
    batch_4_params,
    batch_5_params,
)

BATCHES = [
    ("Batch 1", batch_1_params),
    ("Batch 2", batch_2_params),
    ("Batch 3", batch_3_params),
    ("Batch 4", batch_4_params),
    ("Batch 5", batch_5_params),
]


def print_tool_call(batch_name, params):
    """Print a formatted tool call."""
    print("=" * 80)
    print(f"Execute {batch_name}")
    print("=" * 80)
    print()
    print("Tool: mcp__github__push_files")
    print()
    print("Parameters:")
    print()

    # Print simplified view
    print(f"  owner: {json.dumps(params['owner'])}")
    print(f"  repo: {json.dumps(params['repo'])}")
    print(f"  branch: {json.dumps(params['branch'])}")
    print(f"  message: {json.dumps(params['message'])}")
    print(f"  files: [")

    for i, file_obj in enumerate(params['files']):
        print(f"    {{")
        print(f"      path: {json.dumps(file_obj['path'])},")
        content_preview = file_obj['content'][:50].replace('\n', '\\n')
        print(f"      content: {json.dumps(content_preview + '...')}")
        print(f"    }}" + ("," if i < len(params['files']) - 1 else ""))

    print(f"  ]")
    print()
    print(f"Files in {batch_name}: {len(params['files'])}")
    for file_obj in params['files']:
        print(f"  - {file_obj['path']}")
    print()
    print()


def main():
    print("=" * 80)
    print("GITHUB BATCH PUSH - EXECUTION GUIDE")
    print("=" * 80)
    print()
    print("The following batches are ready to push to:")
    print("  Owner: xxnamae")
    print("  Repo: nordover-ui")
    print("  Branch: main")
    print()
    print(f"Total batches: {len(BATCHES)}")
    print()

    total_files = sum(len(batch[1]['files']) for batch in BATCHES)
    print(f"Total files: {total_files}")
    print()

    print("Execute each batch in sequence using the mcp__github__push_files tool.")
    print()

    for batch_name, params in BATCHES:
        print_tool_call(batch_name, params)

    print("=" * 80)
    print("COMPLETION")
    print("=" * 80)
    print()
    print("After all 5 batches complete successfully:")
    print("  - All 47 files will be on the 'main' branch of xxnamae/nordover-ui")
    print("  - Each commit will have the message:")
    print("    'docs: migrate framework specifications, decisions, and patterns'")
    print()


if __name__ == "__main__":
    main()
