# Execution Reference: How to Use mcp_push_calls.json

## Quick Start

All 44 files have been batched into 9 groups with complete JSON parameters ready to use.

**Files generated:**
- `/home/user/nordover-ui/mcp_push_calls.json` (456KB) - Complete batches with file contents
- `/home/user/nordover-ui/execute_push.py` - Helper script to view batches
- `/home/user/nordover-ui/PUSH_GUIDE.md` - Batch summary table

## Method 1: Inspect Before Pushing

View all batches:
```bash
python execute_push.py
```

View details of a specific batch:
```bash
python execute_push.py 1    # View Batch 1
python execute_push.py 5    # View Batch 5
python execute_push.py 9    # View Batch 9
```

## Method 2: Load JSON Directly in Python

```python
import json

with open('mcp_push_calls.json') as f:
    batches = json.load(f)

# Each batch has this structure:
# {
#   "tool": "mcp__github__push_files",
#   "batch_name": "Batch 1: docs/wiki/topics",
#   "parameters": {
#     "owner": "xxnamae",
#     "repo": "nordover-ui",
#     "branch": "main",
#     "files": [
#       {"path": "...", "content": "..."},
#       ...
#     ],
#     "message": "docs: migrate framework specifications, decisions, and patterns"
#   }
# }

# Process each batch
for batch in batches:
    params = batch['parameters']
    # Call mcp__github__push_files with params
    print(f"Pushing {len(params['files'])} files: {batch['batch_name']}")
```

## Method 3: Use the Tool Directly

Each batch's `parameters` object is ready to pass to `mcp__github__push_files`:

```
Tool: mcp__github__push_files
Parameters from JSON batch['parameters']:
{
  "owner": "xxnamae",
  "repo": "nordover-ui",
  "branch": "main",
  "files": [
    {"path": "docs/wiki/topics/nordover-app-patterns.md", "content": "..."},
    ...
  ],
  "message": "docs: migrate framework specifications, decisions, and patterns"
}
```

## Batch Order & Contents

### Batch 1: docs/wiki/topics (8 files)
- nordover-app-patterns.md
- nordover-arkitektur.md
- nordover-buttons.md
- nordover-elevation.md
- nordover-forms.md
- nordover-layout.md
- nordover-oversikt.md
- nordover-patterns-basis-2.md

### Batch 2: docs/wiki/topics (7 files)
- nordover-patterns-basis.md
- nordover-patterns-parkerte.md
- nordover-patterns-utvidelser-2.md
- nordover-patterns-utvidelser.md
- nordover-rammeverk.md
- nordover-section-patterns.md
- nordover-typografi.md

### Batch 3: docs/wiki/decisions (8 files)
- 2026-05-27-app-patterns-arkitektur.md
- 2026-05-27-buttons-arkitektur.md
- 2026-05-27-elevation-arkitektur.md
- 2026-05-27-forms-arkitektur.md
- 2026-05-27-inter-variable-font.md
- 2026-05-27-layout-primitiver-arkitektur.md
- 2026-05-27-patterns-basis-batch1.md
- 2026-05-27-patterns-basis-batch2.md

### Batch 4: docs/wiki/decisions (8 files)
- 2026-05-27-patterns-parkerte.md
- 2026-05-27-patterns-utvidelser-batch2.md
- 2026-05-27-patterns-utvidelser.md
- 2026-05-27-section-patterns-web.md
- 2026-05-27-to-tokens-pakker.md
- 2026-05-27-tokens-fellesregler.md
- 2026-05-27-tokens-iter-2-moderne-farger-og-tactile.md
- 2026-05-27-tokens-web-scandi-tuning.md

### Batch 5: docs/wiki/decisions (6 files)
- 2026-05-27-typografi-utilities-arkitektur.md
- 2026-05-27-v2-hardening.md
- 2026-05-27-v3-rebuilding.md
- 2026-05-29-nordover-monorepo-distribusjon.md
- 2026-05-29-v3-polish-og-shippable.md
- README.md

### Batch 6: docs/wiki (1 file)
- glossary.md

### Batch 7: docs/handoff (2 files)
- README.md
- monorepo-bootstrap.md

### Batch 8: docs/visual/tokens (1 file)
- README.md

### Batch 9: root (3 files)
- CLAUDE.md
- LICENSE
- README.md

## Key Details

- **All file contents are already embedded** in the JSON — no need to read from disk
- **Valid UTF-8 JSON** — ready to parse and use
- **44 files total** across 9 batches
- **Commit message** is identical for all batches: `"docs: migrate framework specifications, decisions, and patterns"`
- **Target**: `xxnamae/nordover-ui` on the `main` branch

## Error Handling

If a batch fails during push:
1. The JSON file contains the complete batch data for retry
2. Individual batches can be re-pushed without affecting others
3. Use `python execute_push.py N` to verify the batch contents before retry

## Verification

To verify the JSON structure is correct:
```bash
python -m json.tool mcp_push_calls.json > /dev/null && echo "Valid!"
```

To count files per batch:
```bash
python -c "
import json
with open('mcp_push_calls.json') as f:
    for batch in json.load(f):
        files = batch['parameters']['files']
        print(f\"{batch['batch_name']}: {len(files)}\")
"
```
