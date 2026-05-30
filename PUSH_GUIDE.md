# GitHub Push Batching Guide

## Summary
- **Total files**: 44
- **Total batches**: 9
- **Repository**: xxnamae/nordover-ui (main branch)
- **Commit message**: "docs: migrate framework specifications, decisions, and patterns"

## Batch Breakdown

| Batch | Category | Files | Count |
|-------|----------|-------|-------|
| 1 | docs/wiki/topics | nordover-{app-patterns,arkitektur,buttons,elevation,forms,layout,oversikt,patterns-basis-2}.md | 8 |
| 2 | docs/wiki/topics | nordover-{patterns-basis,patterns-parkerte,patterns-utvidelser-2,patterns-utvidelser,rammeverk,section-patterns,typografi}.md | 7 |
| 3 | docs/wiki/decisions | 2026-05-27-{app-patterns,buttons,elevation,forms,inter-variable,layout-primitiver,patterns-basis-batch1,patterns-basis-batch2}-arkitektur.md | 8 |
| 4 | docs/wiki/decisions | 2026-05-27-{patterns-parkerte,patterns-utvidelser-batch2,patterns-utvidelser,section-patterns-web,to-tokens-pakker,tokens-fellesregler,tokens-iter-2,tokens-web-scandi-tuning}.md | 8 |
| 5 | docs/wiki/decisions | 2026-05-27-{typografi-utilities,v2-hardening,v3-rebuilding}.md + 2026-05-29-{nordover-monorepo,v3-polish}.md + README.md | 6 |
| 6 | docs/wiki | glossary.md | 1 |
| 7 | docs/handoff | README.md, monorepo-bootstrap.md | 2 |
| 8 | docs/visual/tokens | README.md | 1 |
| 9 | root | CLAUDE.md, LICENSE, README.md | 3 |

## How to Execute

The Python script `batch_push.py` has generated a complete JSON file at `/home/user/nordover-ui/mcp_push_calls.json` containing all 9 batches with their file contents.

### Option 1: Use in Code
Load the JSON file directly:
```python
import json
with open('mcp_push_calls.json') as f:
    batches = json.load(f)

for batch in batches:
    # Call mcp__github__push_files with batch['parameters']
```

### Option 2: Manual Tool Calls
For each batch in the JSON file:
1. Get the `parameters` object from the batch
2. Call `mcp__github__push_files` with:
   - `owner`: "xxnamae"
   - `repo`: "nordover-ui"
   - `branch`: "main"
   - `files`: [array of {path, content} objects]
   - `message`: "docs: migrate framework specifications, decisions, and patterns"

### Option 3: Inspect Individual Batches
To see files in a specific batch:
```bash
python3 -c "
import json
with open('mcp_push_calls.json') as f:
    batches = json.load(f)
batch = batches[0]  # First batch
print(f\"Batch: {batch['batch_name']}\")
for f in batch['parameters']['files']:
    print(f\"  - {f['path']}\")
"
```

## File Organization

After push, all files will be available at:
- Root: `CLAUDE.md`, `LICENSE`, `README.md`
- Docs structure:
  ```
  docs/
  ├── handoff/
  │   ├── README.md
  │   └── monorepo-bootstrap.md
  ├── visual/tokens/
  │   └── README.md
  ├── wiki/
  │   ├── glossary.md
  │   ├── topics/
  │   │   └── 15 nordover-*.md files
  │   └── decisions/
  │       └── 22 decision files (2026-05-27 & 2026-05-29)
  ```

## Notes
- JSON file is 456KB (valid UTF-8 with all file contents included)
- All file contents are pre-read and embedded in the JSON
- Batches are logically grouped by directory/category
- No binary files; all content is text/markdown
