from PIL import Image, ImageOps
from pathlib import Path

RAW = Path('assets/raw')
OUT = Path('assets/img')
OUT.mkdir(parents=True, exist_ok=True)

# name -> optional crop box as fractions (l,t,r,b) applied before resize
CROPS = {
    'fight-retouch': (0.028, 0.035, 0.972, 0.955),  # remove gpt-image cream border
}

names = ['title-dark','kitchen','drydock','coral','radar','parmesan','shark','fight-retouch',
         'invincible','menu','race','choice','tomorrow','endcard','portrait']
for name in names:
    src = RAW / f'{name}.png'
    im = Image.open(src).convert('RGB')
    w, h = im.size
    box = CROPS.get(name)
    if box:
        im = im.crop((int(w*box[0]), int(h*box[1]), int(w*box[2]), int(h*box[3])))
    im = ImageOps.fit(im, (2560, 1440), method=Image.LANCZOS, centering=(0.5, 0.5))
    out = OUT / f'{name}.jpg'
    im.save(out, quality=90, optimize=True, progressive=True)
    print(out, im.size, out.stat().st_size // 1024, 'KB')

# hero test image stays its own asset
src = RAW / 'test-hero.png'
im = Image.open(src).convert('RGB')
im = ImageOps.fit(im, (2560, 1440), method=Image.LANCZOS, centering=(0.5, 0.5))
out = OUT / 'launch.jpg'
im.save(out, quality=90, optimize=True, progressive=True)
print(out, im.size, out.stat().st_size // 1024, 'KB')

# abyss: keep the circular vignette transparent/cream-free by making outside cream transparent
im = Image.open(RAW / 'abyss.png').convert('RGB')
im = ImageOps.fit(im, (1400, 1400), method=Image.LANCZOS, centering=(0.5, 0.5))
out = OUT / 'abyss.jpg'
im.save(out, quality=90, optimize=True, progressive=True)
print(out, im.size, out.stat().st_size // 1024, 'KB')
