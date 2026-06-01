# CI/CD Integration Guide — Accessibility Testing

This guide explains how the automated accessibility testing integrates with GitHub Actions and the development workflow.

## Overview

The Nordover framework includes a complete accessibility testing pipeline:

```
Code Commit → GitHub Actions → PA11y Scan → Results
                  ↓
            Run on both web & app styleguides
                  ↓
            Critical violations found?
                  ├─ YES → 🔴 Build FAILS (merge blocked)
                  └─ NO → ✅ Build passes (can merge)
                  ↓
            Post PR comment with summary
                  ↓
            Generate downloadable report
```

## GitHub Actions Workflow

**File:** `.github/workflows/a11y-audit.yml`

### When It Runs

- ✅ Every push to `main` branch
- ✅ Every push to `claude/**` branches  
- ✅ Every pull request targeting `main`
- ✅ Weekly scheduled scan (Mondays 09:00 UTC)

### What It Does

1. **Setup** — Install Node.js 18 and PA11y dependencies
2. **Audit** — Run PA11y against both styleguides with WCAG 2.1 AA rules
3. **Report** — Generate JSON results and summary statistics
4. **Comment** — Post results to PR (if it's a PR)
5. **Artifact** — Upload detailed report for download
6. **Status** — Fail build if critical violations found

### Viewing Results

#### In Pull Request

When you submit a PR, the workflow automatically posts a comment:

```
## ✅ Accessibility Audit Results

| Severity | Count |
|----------|-------|
| 🔴 Critical Issues | 0 |
| 🟠 Warnings | 2 |
| 🟡 Notices | 5 |

Standard: WCAG 2.1 Level AA

🔍 Review Details: Open `/docs/visual/accessibility-audit.html` for the interactive audit tool.

✓ No critical issues found.
```

**Click reactions** to acknowledge or comment on the report.

#### In Actions Tab

1. Go to **Actions** tab on GitHub
2. Select **"Accessibility Audit"** workflow
3. Click the workflow run
4. View logs and artifacts

#### Download Detailed Report

1. Go to workflow run
2. Scroll to **Artifacts**
3. Download `a11y-audit-report.zip`
4. Extract and open `index.html` in browser

## Configuration Files

### `.pa11yci.json`

Configures PA11y behavior:

```json
{
  "runners": [
    "axe",           // axe-core accessibility engine
    "htmlcs"         // HTML CodeSniffer
  ],
  "standard": "WCAG2AA",
  "timeout": 10000,  // Wait up to 10s for page load
  "wait": 1000,      // Wait 1s after page loads
  "chromeLaunchConfig": {
    "args": ["--no-sandbox"]  // GitHub Actions Chrome settings
  },
  "urls": [
    "docs/visual/styleguide-web.html",
    "docs/visual/styleguide-app.html"
  ]
}
```

**Key settings:**
- `runners`: Which accessibility engines to use
- `standard`: WCAG 2.1 AA is industry minimum
- `timeout`: Increase if styleguides load slowly
- `urls`: Which pages to audit (both web and app)

### `.github/workflows/a11y-audit.yml`

The workflow file (GitHub Actions automation).

Key steps:
1. **Setup Node.js** — Install runtime
2. **Install dependencies** — Get PA11y, axe, validators
3. **Run PA11y audit** — Scan styleguides with WCAG 2.1 AA rules
4. **Generate report** — Create HTML and JSON reports
5. **Comment PR** — Post summary in PR comment
6. **Upload artifacts** — Store report for download
7. **Fail on critical** — Exit with error if violations found

## Interpreting Results

### Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 Critical | Blocks merge | **MUST fix** before merge |
| 🟠 Warnings | Should address | Fix if possible, document if deferred |
| 🟡 Notices | FYI | Often require manual review |

### Example Results

#### No Issues
```
✅ Accessibility Audit Results
All tests passed! Components meet WCAG 2.1 Level AA.
```

#### With Violations
```
## ❌ Accessibility Audit Results

| Severity | Count |
|----------|-------|
| 🔴 Critical Issues | 3 |
| 🟠 Warnings | 5 |
| 🟡 Notices | 2 |

⚠️ Critical issues found. Please fix before merging.
```

**What to do:**
1. Open `/docs/visual/accessibility-audit.html`
2. Click "Audit Web Styleguide"
3. Find the violations
4. Read remediation guidance
5. Apply fixes to CSS/HTML
6. Re-run audit to verify
7. Push and re-run GitHub Actions

## Handling CI Failures

### Scenario: Build Fails Due to Accessibility

```
❌ Build Failed: Accessibility violations found
   → Critical issues: 2
   → Run audit tool to see details
```

**Steps to resolve:**

1. **Identify violations**
   ```bash
   # Run audit locally
   pa11y-ci --config .pa11yci.json
   ```

2. **Or use interactive tool**
   - Open `docs/visual/accessibility-audit.html`
   - Audit the styleguide
   - Read each violation's remediation

3. **Apply fixes**
   - Edit CSS in `docs/visual/tokens/` or `docs/visual/components/`
   - Update HTML in styleguide if needed

4. **Verify locally**
   ```bash
   # Re-run audit to confirm fix
   pa11y docs/visual/styleguide-web.html --standard WCAG2AA
   ```

5. **Push and re-test**
   ```bash
   git add .
   git commit -m "Fix accessibility violations"
   git push
   ```

6. **Watch Actions tab** — Workflow re-runs automatically

### Scenario: False Positive / Tool Disagreement

If the tool reports an issue that doesn't seem right:

1. **Document** — Add comment in PR explaining why it's not a real violation
2. **Verify** — Check WCAG spec at https://www.w3.org/WAI/WCAG21/quickref/
3. **Consult tool docs** — Confirm tool behavior
4. **Decide** — Fix it to be safe, or document why it's deferred

Example deferral comment:

```
This is a false positive. The component does have keyboard support
via JavaScript event handlers. We use custom widgets which are
ARIA-compliant and tested with screen readers.

Tool: axe-core
Issue: aria-expanded on div (should be button)
Reason: Custom JS handles keyboard interactions equivalent to button
Timeline: Will refactor to native <button> in v2.0
```

## Local Testing (Before PR)

Run the audit locally to catch issues before GitHub Actions:

### Quick Browser Method

```
1. Open docs/visual/accessibility-audit.html in Firefox/Chrome
2. Click "Audit Web Styleguide"
3. Wait for scan to complete
4. Review violations
```

No setup needed.

### Command Line Method

```bash
# Install (one-time)
npm install -g pa11y pa11y-ci axe-core

# Run audit
pa11y-ci --config .pa11yci.json

# Or single page
pa11y docs/visual/styleguide-web.html --standard WCAG2AA
```

### Dockerized Testing

For consistency with CI environment:

```bash
# Run PA11y in Docker
docker run --rm -v $(pwd):/root \
  -w /root \
  node:18 \
  sh -c "npm install -g pa11y pa11y-ci && pa11y-ci --config .pa11yci.json"
```

## Integration with Development Workflow

### For Developers

```
Step 1: Make code changes
Step 2: Create pull request
Step 3: GitHub Actions automatically:
        - Runs accessibility audit
        - Posts results in PR comment
        - Blocks merge if critical issues
Step 4: Review violations in interactive tool
Step 5: Fix issues in code
Step 6: Push changes → Actions re-runs
Step 7: Once passed → Can merge
```

### Best Practices

✅ **Do:**
- Run local audit before pushing (`pa11y-ci`)
- Use interactive tool to understand violations
- Document any deferred non-critical issues
- Re-test after fixes

❌ **Don't:**
- Ignore critical violations
- Skip accessibility testing
- Commit code that fails audit
- Override build status without review

## Customizing the Workflow

### Adding More Styleguides

Edit `.pa11yci.json`:

```json
{
  "urls": [
    "docs/visual/styleguide-web.html",
    "docs/visual/styleguide-app.html",
    "docs/visual/styleguide-custom.html"  // Add here
  ]
}
```

### Changing Severity Levels

In `.github/workflows/a11y-audit.yml`, modify the step "Fail on critical":

```yaml
- name: Fail on critical violations
  if: steps.audit.outputs.critical_violations > 0  # Adjust number
  run: exit 1
```

### Adjusting Timeout

In `.pa11yci.json`, increase `timeout`:

```json
{
  "timeout": 20000  // 20 seconds for slow pages
}
```

### Allowing Warnings

Modify workflow to allow warnings:

```yaml
- name: Fail on violations
  if: steps.audit.outputs.critical_violations > 0 || steps.audit.outputs.warnings > 10
  run: exit 1
```

## Troubleshooting

### Workflow Doesn't Run

**Problem:** Workflow file created but doesn't appear in Actions tab

**Fix:** 
1. Push file to GitHub
2. Go to Actions tab
3. Manually trigger with "Run workflow" button
4. Should appear after next push

### False Positives

**Problem:** Tool flags something that isn't actually a violation

**Solution:**
1. Note the issue ID and rule name
2. Check WCAG spec to confirm
3. Document decision in PR comment
4. Consider updating tool rules if needed

### Styleguide Won't Load

**Problem:** `timeout` exceeded, page didn't load in time

**Solution:**
1. Increase `timeout` in `.pa11yci.json`
2. Check if styleguide is truly loading slowly
3. Optimize styleguide if needed

### Different Results Locally vs. CI

**Problem:** Tool reports different violations locally vs. GitHub Actions

**Cause:** Different browser versions, Node versions, tool versions

**Fix:**
1. Check versions match: `npm list -g pa11y`
2. Update tools: `npm update -g`
3. Use Docker for identical environment
4. Run audit multiple times (some tools have variability)

## Monitoring & Analytics

### Tracking Violations Over Time

1. Create GitHub Discussion for accessibility metrics
2. Screenshot reports before each major release
3. Track trend of new violations vs. fixes
4. Set team goals for violation reduction

### Quarterly Report

Generate quarterly summary:
- Violations found and fixed
- Tools and standards used
- Team training completed
- Customer accessibility feedback
- Roadmap for next quarter

## CI/CD Best Practices

### Pre-merge Requirements

Make accessibility audit a required check:

1. Go to repo **Settings** → **Branches**
2. Click **Add rule** under branch protection
3. Set `main` as pattern
4. Under **Require status checks**:
   - ✅ Check "Accessibility Audit"
   - ✅ Check "CSS & HTML Validation"
   - ✅ Check other desired checks

### Documentation

Keep audit results documented:

1. Merge results into `/docs/visual/ACCESSIBILITY-AUDIT-RESULTS.md`
2. Tag releases with audit results in release notes
3. Link PR to GitHub Discussions for accessibility
4. Create issues for known violations to track

### Regular Audits

Schedule recurring testing:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Every Monday at 09:00 UTC
```

This generates reports even without code changes.

## Next Steps

1. ✅ Commit workflow file (`.github/workflows/a11y-audit.yml`)
2. ✅ Commit config file (`.pa11yci.json`)
3. ✅ Push to GitHub
4. ✅ Create test PR to verify workflow runs
5. ✅ Set as required status check
6. ✅ Celebrate automated accessibility testing! 🎉

---

**Workflow Version:** 1.0  
**Updated:** 2026-06-01  
**Maintainer:** Nordover Team
