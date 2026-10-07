"""Fill the QR squares on the print sheets.

Each square is written as
    <div class="qr" data-href="URL"><div class="box"></div><div class="cap">...</div></div>
and this script draws the code for URL inside the box as inline SVG. Run it
from this folder after adding or changing a square, then render the PDFs.
Requires segno (pip install segno).
"""
import glob
import io
import re

import segno

BOX = re.compile(r'(<div class="qr" data-href="([^"]+)">)<div class="box[^"]*">.*?</div>(<div class="cap">)', re.S)


def svg(url):
    buf = io.BytesIO()
    segno.make(url, error='m', micro=False).save(buf, kind='svg', border=1, omitsize=True,
                                                xmldecl=False, svgns=True, nl=False)
    return buf.getvalue().decode('utf-8')


def fill(m):
    return f'{m.group(1)}<div class="box code">{svg(m.group(2))}</div>{m.group(3)}'


for path in sorted(glob.glob('*.html')):
    text = open(path, encoding='utf-8').read()
    new, n = BOX.subn(fill, text)
    if n:
        open(path, 'w', encoding='utf-8').write(new)
        print(f'{path}: {n}')
