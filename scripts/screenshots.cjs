#!/usr/bin/env node
/* Visual verification harness — render the styleguide + examples at the three
 * official QA breakpoints (mobile <480 / tablet 768-1024 / desktop >1024), in
 * both light and dark mode, and write PNGs to /tmp/nordover-shots/.
 *
 * Self-contained:
 *  - Resolves the `playwright` module whether it's a local/global install or
 *    this managed environment's global node_modules.
 *  - Uses a pre-installed Chromium at /opt/pw-browsers when present, otherwise
 *    Playwright's default browser cache (run `npx playwright install chromium`).
 *  - Auto-starts a static server on :8000 if one isn't already responding, and
 *    shuts it down on exit.
 *
 *   node scripts/screenshots.cjs          (or: npm run shots)
 */
const fs = require('fs');
const http = require('http');
const { spawn, execSync } = require('child_process');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PORT = Number(process.env.PORT || 8000);
const BASE = process.env.BASE_URL || `http://localhost:${PORT}`;
const OUT = process.env.SHOTS_DIR || '/tmp/nordover-shots';

// --- Resolve Chromium location (prefer this env's pre-installed browsers) ---
if (!process.env.PLAYWRIGHT_BROWSERS_PATH && fs.existsSync('/opt/pw-browsers')) {
  process.env.PLAYWRIGHT_BROWSERS_PATH = '/opt/pw-browsers';
}

// --- Resolve the playwright module from a few likely locations ---
function loadPlaywright() {
  const candidates = [
    'playwright',                                   // local / NODE_PATH
    '/opt/node22/lib/node_modules/playwright',      // this env's global
  ];
  try {
    const g = execSync('npm root -g', { encoding: 'utf8' }).trim();
    if (g) candidates.push(path.join(g, 'playwright'));
  } catch { /* ignore */ }
  for (const c of candidates) {
    try { return require(c); } catch { /* try next */ }
  }
  console.error(
    'Could not load the "playwright" module.\n' +
    'Install it with:  npm i -D playwright && npx playwright install chromium'
  );
  process.exit(1);
}

// --- Ensure a static server is serving the repo on PORT ---
function ping(url) {
  return new Promise((resolve) => {
    const req = http.get(url, (res) => { res.resume(); resolve(res.statusCode === 200); });
    req.on('error', () => resolve(false));
    req.setTimeout(1500, () => { req.destroy(); resolve(false); });
  });
}

async function ensureServer() {
  const probe = `${BASE}/docs/visual/styleguide.html`;
  if (await ping(probe)) return null; // already up — leave it running
  const srv = spawn('python3', ['-m', 'http.server', String(PORT)], {
    cwd: ROOT, stdio: 'ignore', detached: false,
  });
  // wait up to ~10s for it to come up
  for (let i = 0; i < 40; i++) {
    await new Promise((r) => setTimeout(r, 250));
    if (await ping(probe)) return srv;
  }
  srv.kill();
  throw new Error(`could not start static server on :${PORT}`);
}

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
  const { chromium } = loadPlaywright();
  let server = null;
  try {
    server = await ensureServer();
    fs.mkdirSync(OUT, { recursive: true });
    const browser = await chromium.launch();
    const shots = [];
    for (const [name, route] of PAGES) {
      for (const [vp, w, h] of VIEWPORTS) {
        for (const mode of ['light', 'dark']) {
          const ctx = await browser.newContext({
            viewport: { width: w, height: h },
            deviceScaleFactor: 1,
            reducedMotion: 'reduce', // freeze entrance animations for stable frames
          });
          const page = await ctx.newPage();
          await page.goto(BASE + route, { waitUntil: 'networkidle', timeout: 30000 });
          if (mode === 'dark') {
            await page.evaluate(() => {
              const cb = document.getElementById('dark');
              if (cb) { cb.checked = true; cb.dispatchEvent(new Event('change', { bubbles: true })); }
            });
          }
          await page.waitForTimeout(350); // let theme + fonts settle
          const file = `${OUT}/${name}-${vp}-${mode}.png`;
          await page.screenshot({ path: file, fullPage: name !== 'styleguide' });
          shots.push(file);
          await ctx.close();
        }
      }
    }
    await browser.close();
    console.log('wrote ' + shots.length + ' screenshots to ' + OUT);
    shots.forEach((s) => console.log('  ' + s));
  } finally {
    if (server) server.kill(); // only kill a server we started
  }
})().catch((err) => { console.error(err); process.exit(1); });
