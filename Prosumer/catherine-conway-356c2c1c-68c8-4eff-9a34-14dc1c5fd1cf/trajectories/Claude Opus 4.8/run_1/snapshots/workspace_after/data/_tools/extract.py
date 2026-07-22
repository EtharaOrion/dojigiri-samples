#!/usr/bin/env python3
import sys, zipfile, re, os
from xml.etree import ElementTree as ET

def strip_ns(tag):
    return tag.split('}')[-1]

def xlsx_to_rows(path):
    z = zipfile.ZipFile(path)
    # shared strings
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        root = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in root:
            txt = ''.join(t.text or '' for t in si.iter() if strip_ns(t.tag)=='t')
            shared.append(txt)
    # find sheets
    out = {}
    for name in z.namelist():
        if re.match(r'xl/worksheets/sheet\d+\.xml', name):
            root = ET.fromstring(z.read(name))
            rows = []
            for row in root.iter():
                if strip_ns(row.tag) != 'row':
                    continue
                cells = []
                for c in row:
                    if strip_ns(c.tag) != 'c':
                        continue
                    ref = c.get('r','')
                    t = c.get('t','')
                    v = None
                    for ch in c:
                        if strip_ns(ch.tag) == 'v':
                            v = ch.text
                        elif strip_ns(ch.tag) == 'is':
                            v = ''.join(x.text or '' for x in ch.iter() if strip_ns(x.tag)=='t')
                    if v is None:
                        val = ''
                    elif t == 's':
                        val = shared[int(v)]
                    else:
                        val = v
                    col = re.match(r'([A-Z]+)', ref).group(1) if ref else ''
                    cells.append((col, val))
                rows.append(cells)
            out[name] = rows
    return out

def docx_to_text(path):
    z = zipfile.ZipFile(path)
    parts = []
    for name in z.namelist():
        if name.startswith('word/') and name.endswith('.xml') and ('document' in name or 'header' in name or 'footer' in name):
            root = ET.fromstring(z.read(name))
            for p in root.iter():
                if strip_ns(p.tag) == 'p':
                    txt = ''.join(t.text or '' for t in p.iter() if strip_ns(t.tag)=='t')
                    if txt.strip():
                        parts.append(txt)
                if strip_ns(p.tag) == 'tbl':
                    pass
    # tables: iterate rows
    return '\n'.join(parts)

def docx_full(path):
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read('word/document.xml'))
    lines = []
    def walk(el):
        tag = strip_ns(el.tag)
        if tag == 'tbl':
            for tr in el.iter():
                if strip_ns(tr.tag)=='tr':
                    cells=[]
                    for tc in tr:
                        if strip_ns(tc.tag)=='tc':
                            txt=''.join(t.text or '' for t in tc.iter() if strip_ns(t.tag)=='t')
                            cells.append(txt)
                    lines.append(' | '.join(cells))
            return
        if tag == 'p':
            txt=''.join(t.text or '' for t in el.iter() if strip_ns(t.tag)=='t')
            lines.append(txt)
            return
        for ch in el:
            walk(ch)
    body = None
    for ch in root:
        if strip_ns(ch.tag)=='body':
            body=ch
    for ch in body:
        walk(ch)
    return '\n'.join(lines)

def pptx_to_text(path):
    z = zipfile.ZipFile(path)
    parts = []
    slides = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml', n)],
                    key=lambda x: int(re.search(r'(\d+)', x).group(1)))
    for name in slides:
        root = ET.fromstring(z.read(name))
        txt = []
        for t in root.iter():
            if strip_ns(t.tag) == 't':
                txt.append(t.text or '')
        parts.append('=== %s ===' % name + '\n' + ' '.join(txt))
    return '\n'.join(parts)

def main():
    for path in sys.argv[1:]:
        print('\n\n########## FILE: %s ##########' % path)
        ext = path.lower().rsplit('.',1)[-1]
        try:
            if ext == 'xlsx':
                out = xlsx_to_rows(path)
                for sheet, rows in out.items():
                    print('--- sheet %s ---' % sheet)
                    for r in rows:
                        print(' | '.join('%s=%s'%(c,v) for c,v in r))
            elif ext == 'docx':
                print(docx_full(path))
            elif ext == 'pptx':
                print(pptx_to_text(path))
            elif ext in ('tsv','csv','xml','html','txt'):
                with open(path, encoding='utf-8', errors='replace') as f:
                    print(f.read())
        except Exception as e:
            print('ERROR:', e)

if __name__ == '__main__':
    main()
