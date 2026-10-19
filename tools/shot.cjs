// Screenshot one or more times from a frame preview using an already-running Chrome.
// Usage: node tools/shot.cjs <preview.html> <out.png> <time> [time...]
const path = require('path');
const puppeteer = require(path.resolve('D:/WorkSpace/.npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core'));

(async () => {
  const [, , file, out, ...times] = process.argv;
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
  const page = await browser.newPage();
  page.on('console', (m) => {
    if (m.type() === 'error') console.log('PAGE ERROR:', m.text());
  });
  page.on('pageerror', (e) => console.log('PAGE EXCEPTION:', e.message));
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  const url = 'file:///' + path.resolve(file).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);
  await new Promise((r) => setTimeout(r, 900));
  const t = times.length ? parseFloat(times[0]) : 0;
  await page.evaluate((tt) => {
    const ids = Object.keys(window.__timelines || {});
    if (!ids.length) throw new Error('no timelines');
    const tl = window.__timelines[ids[0]];
    tl.pause();
    tl.seek(tt);
    return ids[0];
  }, t);
  await new Promise((r) => setTimeout(r, 260));
  await page.screenshot({ path: path.resolve(out), type: 'png' });
  console.log('shot', out, 'at', t, 'timeline', await page.evaluate(() => Object.keys(window.__timelines || {})));
  await page.close();
  await browser.disconnect();
})().catch((e) => {
  console.error('SHOT FAILED', e);
  process.exit(1);
});
