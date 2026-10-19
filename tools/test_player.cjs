const path = require('path');
const puppeteer = require(path.resolve('D:/WorkSpace/.npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core'));

(async () => {
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
  const page = await browser.newPage();
  const errors = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push('EXC ' + e.message));
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto('http://127.0.0.1:8080/player.html', { waitUntil: 'networkidle2', timeout: 120000 });
  await new Promise((r) => setTimeout(r, 5000));
  const info = await page.evaluate(() => {
    const fs = [...document.querySelectorAll('iframe')];
    return {
      iframes: fs.length,
      timelines: fs.map((f) => {
        try { return Object.keys(f.contentWindow.__timelines || {}); } catch (e) { return ['ERR ' + e.message]; }
      }),
      error: document.getElementById('error').textContent
    };
  });
  console.log(JSON.stringify(info, null, 2));
  await page.click('#start').catch((e) => console.log('start click failed', e.message));
  await new Promise((r) => setTimeout(r, 6000));
  await page.screenshot({ path: 'analysis/player-06.png' });
  const state = await page.evaluate(() => ({
    t: document.getElementById('audio').currentTime,
    paused: document.getElementById('audio').paused,
    active: [...document.querySelectorAll('iframe')].findIndex((f) => f.style.display !== 'none'),
    error: document.getElementById('error').textContent
  }));
  console.log(JSON.stringify(state));
  await page.evaluate(() => { document.getElementById('audio').currentTime = 100; });
  await new Promise((r) => setTimeout(r, 2500));
  await page.screenshot({ path: 'analysis/player-100.png' });
  console.log('errors', errors.slice(0, 10));
  await page.close();
  await browser.disconnect();
})().catch((e) => { console.error('FAIL', e); process.exit(1); });
