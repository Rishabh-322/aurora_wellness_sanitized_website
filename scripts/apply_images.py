#!/usr/bin/env python3
"""Activate or reset placeholder images in this static project. Standard library only.

Usage:
  python3 scripts/apply_images.py
  python3 scripts/apply_images.py --reset
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
RESET = "--reset" in sys.argv

# The image slot's opening tag includes its class, data-file, and data-alt values.
SLOT = re.compile(r'(<div\b(?=[^>]*\bclass="[^"]*\bimage-slot\b[^\"]*")(?=[^>]*\bdata-file="([^"]+)")(?=[^>]*\bdata-alt="([^"]+)")[^>]*>)(.*?)(</div>)', re.S)

page = PAGE.read_text(encoding="utf-8")
changed = [0]

def rewrite(match):
    opening, filename, label, inside, closing = match.groups()
    filename = html.unescape(filename)
    label = html.unescape(label)
    if not filename.startswith('assets/') or '..' in Path(filename).parts:
        raise ValueError(f"Unsafe asset path: {filename}")
    f = ROOT / filename
    # Unsupported formats never get embedded accidentally.
    has_image = not RESET and f.is_file() and f.suffix.lower() in {'.webp','.png','.jpg','.jpeg','.avif'}
    if has_image:
        opening = re.sub(r'\bclass="([^"]*)"', lambda m:'class="'+ ' '.join(dict.fromkeys((m.group(1)+' has-image').split()))+'"', opening,count=1)
        # The alt is intentionally generic. Do not name or depict real people without rights.
        content = (f'<span class="image-slot-label">{html.escape(label)}</span>'
          +f'<img class="slot-image" loading="lazy" decoding="async" src="{html.escape(filename,quote=True)}" alt="{html.escape(label,quote=True)}">')
    else:
        opening = re.sub(r'\bclass="([^"]*)"', lambda m:'class="'+ ' '.join(w for w in m.group(1).split() if w!='has-image')+'"', opening,count=1)
        content = f'<span class="image-slot-label">{html.escape(label)}</span>'
    changed[0] += 1
    return opening+content+closing

new_page = SLOT.sub(rewrite,page)
if changed[0]==0:
    raise SystemExit('No image slots found. No changes made.')
PAGE.write_text(new_page,encoding='utf-8')
print(f"Processed {changed[0]} image slots. Mode: {'placeholders' if RESET else 'activate available files'}.")
