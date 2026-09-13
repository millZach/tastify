// Capture matched screenshots of the trial builds.
// Usage: node capture.mjs  (run from a folder that has playwright installed, e.g. design-6-skill)
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const OUT = resolve(process.env.OUT || '/home/zach/projects/design-skill/examples/captures');
mkdirSync(OUT, { recursive: true });

const SITES = [
  { pair: 'ember',    cond: 'baseline', port: 4301 },
  { pair: 'ember',    cond: 'tastify',  port: 4302 },
  { pair: 'foldline', cond: 'baseline', port: 4303 },
  { pair: 'foldline', cond: 'tastify',  port: 4304 },
  { pair: 'orrery',   cond: 'baseline', port: 4305 },
  { pair: 'orrery',   cond: 'tastify',  port: 4306 },
  { pair: 'redrising', cond: 'baseline', port: 4321 },
  { pair: 'redrising', cond: 'tastify',  port: 4322 },
  { pair: 'pip',      cond: 'baseline', port: 4323 },
  { pair: 'pip',      cond: 'tastify',  port: 4324 },
];
// ONLY=redrising,pip limits the run to those pairs.
const ONLY = process.env.ONLY ? process.env.ONLY.split(',') : null;
const WAIT = Number(process.env.WAIT || 2500);

const VIEWS = [
  { name: 'desktop', width: 1440, height: 900, mobile: false },
  { name: 'phone',   width: 390,  height: 844, mobile: true },
];

// Software GL keeps canvas-heavy pages from crashing the headless GPU process.
const browser = await chromium.launch({ args: ['--enable-unsafe-swiftshader', '--use-angle=swiftshader'] });
for (const site of SITES.filter((s) => !ONLY || ONLY.includes(s.pair))) {
  for (const view of VIEWS) {
    const ctx = await browser.newContext({
      viewport: { width: view.width, height: view.height },
      deviceScaleFactor: 2,
      isMobile: view.mobile,
      hasTouch: view.mobile,
      reducedMotion: 'no-preference',
    });
    const page = await ctx.newPage();
    const url = `http://127.0.0.1:${site.port}/`;
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(WAIT); // let entry animations settle
    const file = `${OUT}/${site.pair}-${site.cond}-${view.name}.png`;
    await page.screenshot({ path: file, fullPage: false });
    console.log('saved', file);
    await ctx.close();
  }
}
await browser.close();
