#!/usr/bin/env python3
"""
Load and display batches from mcp_push_calls.json for execution.
This demonstrates how to use the generated batch data.
"""

import json
from pathlib import Path

def load_batches():
    """Load all batches from the generated JSON file."""
    with open(Path(__file__).parent / 'mcp_push_calls.json') as f:
        return json.load(f)

def show_batch(batch_num):
    """Display a specific batch."""
    batches = load_batches()
    if batch_num < 1 or batch_num > len(batches):
        print(f"Invalid batch number. Valid range: 1-{len(batches)}")
        return
    
    batch = batches[batch_num - 1]
    params = batch['parameters']
    
    print(f"\n{batch['batch_name']}")
    print("=" * 80)
    print(f"Files to push: {len(params['files'])}\n")
    
    for file_obj in params['files']:
        print(f"  - {file_obj['path']}")
    
    print(f"\nParameters ready for mcp__github__push_files:")
    print(f"  owner: {params['owner']}")
    print(f"  repo: {params['repo']}")
    print(f"  branch: {params['branch']}")
    print(f"  message: {params['message']}")
    print(f"  files: [array with {len(params['files'])} items]")

def show_all_batches():
    """Display all batches summary."""
    batches = load_batches()
    print("\nAll Batches")
    print("=" * 80)
    
    total_files = 0
    for i, batch in enumerate(batches, 1):
        files = batch['parameters']['files']
        total_files += len(files)
        print(f"{i:2d}. {batch['batch_name']:45s} {len(files):2d} files")
    
    print("-" * 80)
    print(f"{'TOTAL':47s} {total_files:2d} files")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        show_batch(int(sys.argv[1]))
    else:
        show_all_batches()
        print("\nUsage:")
        print(f"  python {Path(__file__).name}        # Show all batches")
        print(f"  python {Path(__file__).name} 1      # Show batch 1 details")
        print(f"  python {Path(__file__).name} 5      # Show batch 5 details")
