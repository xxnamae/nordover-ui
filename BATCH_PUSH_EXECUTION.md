# Batch Push Execution Guide

## Summary

Your 47 files have been organized into **5 batches** with the following distribution:

- **Batch 1**: 10 files (109.9 KB) - Root files + app-patterns, arkitektur, buttons, elevation
- **Batch 2**: 10 files (163.4 KB) - Forms, layout, patterns (basis, parkerte, utvidelser)
- **Batch 3**: 10 files (57.4 KB) - Typografi + decisions (app-patterns through patterns-parkerte)
- **Batch 4**: 10 files (53.7 KB) - Decisions (patterns-utvidelser through v3-rebuilding)
- **Batch 5**: 7 files (50.2 KB) - Final decisions, visual tokens, glossary, handoff docs

**Total**: 434.6 KB across all batches

## Batch Details

See `/home/user/nordover-ui/batch_manifest.py` output above for exact file listing by batch.

## Execution Steps

The parameters for all batches are stored in `/home/user/nordover-ui/BATCH_PARAMETERS.py` as Python dictionaries:
- `batch_1_params`
- `batch_2_params`
- `batch_3_params`
- `batch_4_params`
- `batch_5_params`

### Option 1: Execute via Claude Code Agent

You can copy the parameters from `BATCH_PARAMETERS.py` and call:

```python
mcp__github__push_files(
    owner="xxnamae",
    repo="nordover-ui",
    branch="main",
    files=[...],
    message="docs: migrate framework specifications, decisions, and patterns"
)
```

for each batch sequentially.

### Option 2: Extract Parameters to JSON

To get just the JSON parameters for direct use:

```bash
python3 /home/user/nordover-ui/extract_batches.py > batches.py
# Then extract batch_N_params and use as JSON
```

## Notes

- All file paths are relative to repository root
- File content encoding is UTF-8 (handles markdown with Unicode)
- Each batch stays under 200 KB JSON size limit
- Files are grouped logically: root → topics → decisions → other docs
- Commit message is consistent: "docs: migrate framework specifications, decisions, and patterns"

## File Organization

```
Batch 1: Root files + core architecture topics
├── CLAUDE.md, LICENSE, README.md
├── EXECUTION_REFERENCE.md, PUSH_GUIDE.md, BATCH_PUSH_INDEX.md
└── docs/wiki/topics/nordover-*.md (app-patterns, arkitektur, buttons, elevation)

Batch 2: Patterns and forms topics
└── docs/wiki/topics/nordover-*.md (forms, layout, oversikt, patterns-*, rammeverk, section-patterns)

Batch 3: Typography + early decisions
├── docs/wiki/topics/nordover-typografi.md
└── docs/wiki/decisions/*.md (app-patterns through patterns-parkerte)

Batch 4: Mid-range decisions
└── docs/wiki/decisions/*.md (patterns-utvidelser through v3-rebuilding)

Batch 5: Final decisions + reference docs
├── docs/wiki/decisions/*.md (nordover-monorepo, v3-polish, README)
├── docs/visual/tokens/README.md
├── docs/wiki/glossary.md
└── docs/handoff/*.md (monorepo-bootstrap, README)
```
