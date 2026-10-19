// Download a batch of Labnana task results into assets/raw.
// Usage: node tools/download_images.cjs name=url name=url ...
const https = require('https');
const fs = require('fs');
const path = require('path');

const dir = path.resolve(__dirname, '..', 'assets', 'raw');
fs.mkdirSync(dir, { recursive: true });

function get(url, redirects = 0) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'user-agent': 'Mozilla/5.0' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location && redirects < 5) {
        return resolve(get(res.headers.location, redirects + 1));
      }
      if (res.statusCode !== 200) return reject(new Error('status ' + res.statusCode + ' ' + url));
      const chunks = [];
      res.on('data', (d) => chunks.push(d));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    }).on('error', reject);
  });
}

(async () => {
  for (const arg of process.argv.slice(2)) {
    const i = arg.indexOf('=');
    const name = arg.slice(0, i);
    const url = arg.slice(i + 1);
    try {
      const buf = await get(url);
      const out = path.join(dir, name + '.png');
      fs.writeFileSync(out, buf);
      console.log('saved', out, buf.length);
    } catch (e) {
      console.error('FAIL', name, e.message);
    }
  }
})();
