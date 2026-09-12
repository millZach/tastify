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
];

const VIEWS = [
  { name: 'desktop', width: 1440, height: 900, mobile: false },
  { name: 'phone',   width: 390,  height: 844, mobile: true },
];

const browser = await chromium.launch();
for (const site of SITES) {
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
    await page.waitForTimeout(2500); // let entry animations settle
    const file = `${OUT}/${site.pair}-${site.cond}-${view.name}.png`;
    await page.screenshot({ path: file, fullPage: false });
    console.log('saved', file);
    await ctx.close();
  }
}
await browser.close();
