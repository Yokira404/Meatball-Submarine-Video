// Vendor Google Fonts (woff2 + a local fonts.css) so the composition renders offline.
const https = require('https');
const fs = require('fs');
const path = require('path');

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36';
const CSS_URL = 'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,900;1,9..144,600;1,9..144,900&family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap';

function get(url, headers = {}) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return resolve(get(res.headers.location, headers));
      }
      let chunks = [];
      res.on('data', (d) => chunks.push(d));
      res.on('end', () => resolve({ status: res.statusCode, body: Buffer.concat(chunks) }));
    }).on('error', reject);
  });
}

(async () => {
  const outDir = path.resolve(__dirname, '..', 'public', 'fonts');
  fs.mkdirSync(outDir, { recursive: true });
  const css = await get(CSS_URL, { 'User-Agent': UA });
  let text = css.body.toString('utf8');
  if (css.status !== 200) throw new Error('css status ' + css.status);
  const urls = [...text.matchAll(/url\((https:\/\/[^)]+\.woff2)\)/g)].map((m) => m[1]);
  const uniq = [...new Set(urls)];
  const map = new Map();
  let i = 0;
  for (const u of uniq) {
    const name = `font-${String(i++).padStart(2, '0')}.woff2`;
    const r = await get(u, { 'User-Agent': UA });
    if (r.status !== 200) throw new Error('font status ' + r.status + ' ' + u);
    fs.writeFileSync(path.join(outDir, name), r.body);
    map.set(u, `fonts/${name}`);
    console.log('saved', name, r.body.length);
  }
  text = text.replace(/url\((https:\/\/[^)]+\.woff2)\)/g, (m, u) => `url(${map.get(u)})`);
  fs.writeFileSync(path.join(outDir, 'fonts.css'), text, 'utf8');
  console.log('css written', text.length);
})();
