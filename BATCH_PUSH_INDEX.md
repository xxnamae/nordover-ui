# Batch Push Index

This directory contains all files and tools needed to push 44 documentation files to `xxnamae/nordover-ui` on the main branch.

## Generated Files

### 1. `mcp_push_calls.json` (456KB)
**Main data file** — Contains all 9 batches with complete file contents, ready for the `mcp__github__push_files` tool.

Structure:
```json
[
  {
    "tool": "mcp__github__push_files",
    "batch_name": "Batch N: ...",
    "parameters": {
      "owner": "xxnamae",
      "repo": "nordover-ui",
      "branch": "main",
      "files": [
        {"path": "...", "content": "..."},
        ...
      ],
      "message": "docs: migrate framework specifications, decisions, and patterns"
    }
  },
  ...
]
```

### 2. `execute_push.py` (2.0KB)
**Helper script** — Displays batch contents without loading large file contents.

Usage:
```bash
python execute_push.py        # Show summary of all 9 batches
python execute_push.py 1      # Show detailed view of Batch 1
python execute_push.py 9      # Show detailed view of Batch 9
```

### 3. `PUSH_GUIDE.md` (3.2KB)
**Quick reference** — Summary table of all batches with file counts and commit details.

### 4. `EXECUTION_REFERENCE.md` (4.5KB)
**Complete documentation** — How to load, inspect, and execute the batches.

### 5. `BATCH_PUSH_INDEX.md` (this file)
**Navigation guide** — Overview of all generated files.

## Quick Start

### Step 1: Verify the Data
```bash
python execute_push.py
```
Shows all 9 batches with file counts.

### Step 2: Inspect a Batch
```bash
python execute_push.py 1
```
Shows files in Batch 1 and the parameters ready for the tool.

### Step 3: Execute Pushes

Load from JSON and call `mcp__github__push_files` for each batch:

```python
import json

with open('mcp_push_calls.json') as f:
    batches = json.load(f)

for batch in batches:
    # Call mcp__github__push_files with batch['parameters']
    pass
```

Or use the tool directly with parameters from any batch in the JSON file.

## Summary

| Item | Count |
|------|-------|
| Total files | 44 |
| Total batches | 9 |
| Docs files | 41 |
| Root files | 3 |
| JSON size | 456KB |

## Batch Breakdown

- **Batch 1-2**: `docs/wiki/topics/` — 15 topic specification files
- **Batch 3-5**: `docs/wiki/decisions/` — 22 architecture decision records
- **Batch 6**: `docs/wiki/` — glossary.md
- **Batch 7**: `docs/handoff/` — 2 implementation guides
- **Batch 8**: `docs/visual/tokens/` — 1 token specification
- **Batch 9**: Root files — CLAUDE.md, LICENSE, README.md

## File Contents Preview

All file contents are:
- Pre-read and embedded in JSON (no disk I/O needed during push)
- UTF-8 encoded
- Markdown or text format
- Ready to use immediately

## Execution Methods

### Method A: Use Python Script
```bash
python execute_push.py          # View batches
# Then load mcp_push_calls.json and iterate
```

### Method B: Load JSON Directly
```python
import json
with open('mcp_push_calls.json') as f:
    for batch in json.load(f):
        # batch['parameters'] ready for tool call
```

### Method C: Manual Tool Calls
Extract `parameters` from any batch in the JSON and pass to `mcp__github__push_files`.

## Notes

- Batches are logically organized by directory/category
- All files belong to the `docs/` folder or root of the repository
- Commit message is identical across all batches
- No binary files — all content is text/markdown
- Valid JSON — verified with `python -m json.tool`

## Next Steps

1. Run `python execute_push.py` to see batch summary
2. Review specific batches with `python execute_push.py N`
3. Load `mcp_push_calls.json` in your execution environment
4. Call `mcp__github__push_files` for each batch
5. Verify files appear in the GitHub repository

---

**Generated**: 2026-05-30  
**Repository**: xxnamae/nordover-ui  
**Target Branch**: main  
**Commit Message**: "docs: migrate framework specifications, decisions, and patterns"
