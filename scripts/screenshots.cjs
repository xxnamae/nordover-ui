#!/usr/bin/env node
/* Visual verification harness — render the styleguide + examples at the three
 * official QA breakpoints (mobile <480 / tablet 768-1024 / desktop >1024), in
 * both light and dark mode, and write PNGs to /tmp/nordover-shots/.
 *
 * No browser in PATH, but Playwright's Chromium ships at /opt/pw-browsers and
 * the package lives in the global node_modules — both are referenced explicitly
 * so this runs without a project-local install.
 *
 *   PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node scripts/screenshots.cjs
 *
 * Assumes a static server on http://localhost:8000 rooted at the repo.
 */
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');

const OUT = '/tmp/nordover-shots';
const BASE = process.env.BASE_URL || 'http://localhost:8000';

const PAGES = [
  ['styleguide', '/docs/visual/styleguide.html'],
  ['marketing',  '/docs/examples/marketing-landing.html'],
  ['dashboard',  '/docs/examples/saas-dashboard.html'],
];
const VIEWPORTS = [
  ['mobile', 390, 844],
  ['tablet', 834, 1112],
  ['desktop', 1440, 900],
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const shots = [];
  for (const [name, path] of PAGES) {
    for (const [vp, w, h] of VIEWPORTS) {
      for (const mode of ['light', 'dark']) {
        const ctx = await browser.newContext({
          viewport: { width: w, height: h },
          deviceScaleFactor: 1,
          reducedMotion: 'reduce', // freeze entrance animations for stable frames
        });
        const page = await ctx.newPage();
        await page.goto(BASE + path, { waitUntil: 'networkidle', timeout: 30000 });
        if (mode === 'dark') {
          // Every Nordover page toggles dark via a checkbox#dark
          await page.evaluate(() => {
            const cb = document.getElementById('dark');
            if (cb) { cb.checked = true; cb.dispatchEvent(new Event('change', { bubbles: true })); }
          });
        }
        await page.waitForTimeout(350); // let theme + fonts settle
        const file = `${OUT}/${name}-${vp}-${mode}.png`;
        // Full page for examples/styleguide top; cap height so files stay viewable
        await page.screenshot({ path: file, fullPage: name !== 'styleguide' });
        shots.push(file);
        await ctx.close();
      }
    }
  }
  await browser.close();
  console.log('wrote ' + shots.length + ' screenshots to ' + OUT);
  shots.forEach((s) => console.log('  ' + s));
})();
