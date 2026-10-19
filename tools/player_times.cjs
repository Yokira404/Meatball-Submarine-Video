const path = require('path');
const puppeteer = require(path.resolve('D:/WorkSpace/.npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core'));

(async () => {
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto('http://127.0.0.1:8080/player.html', { waitUntil: 'networkidle2', timeout: 120000 });
  await new Promise((r) => setTimeout(r, 3500));
  await page.click('#start');
  await new Promise((r) => setTimeout(r, 800));
  const times = [11.5, 22.6, 33.8, 46.7, 57.7, 68.9, 79.7, 93.3, 103.9, 126.2, 151.2, 163.9, 169.2, 181.0];
  for (const t of times) {
    await page.evaluate((tt) => {
      const a = document.getElementById('audio');
      a.currentTime = tt;
      a.play();
    }, t);
    await new Promise((r) => setTimeout(r, 550));
    const state = await page.evaluate(() => {
      const f = [...document.querySelectorAll('iframe')];
      return { t: document.getElementById('audio').currentTime, active: f.findIndex((x) => x.style.display !== 'none') };
    });
    const name = 'analysis/player-' + String(t).replace('.', '_') + '.png';
    await page.screenshot({ path: name });
    console.log(t, JSON.stringify(state));
  }
  await page.close();
  await browser.disconnect();
})().catch((e) => { console.error('FAIL', e); process.exit(1); });
