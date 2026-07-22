import sys, zipfile, re, os
from xml.etree import ElementTree as ET

def strip_ns(t):
    return re.sub(r'\{[^}]*\}', '', t)

def xlsx_dump(path):
    out=[]
    z=zipfile.ZipFile(path)
    # shared strings
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        r=ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in r:
            txt=''.join(t.text or '' for t in si.iter() if strip_ns(t.tag)=='t')
            shared.append(txt)
    # workbook sheet names
    names={}
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    sheets=[s for s in wb.iter() if strip_ns(s.tag)=='sheet']
    rels={}
    if 'xl/_rels/workbook.xml.rels' in z.namelist():
        rr=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        for rel in rr:
            rels[rel.get('Id')]=rel.get('Target')
    sheetfiles=[]
    wsfiles=sorted([n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$',n)],
                   key=lambda x:int(re.search(r'(\d+)',x.split('/')[-1]).group()))
    names_list=[s.get('name') for s in sheets]
    for i,tgt in enumerate(wsfiles):
        nm=names_list[i] if i<len(names_list) else tgt
        sheetfiles.append((nm,tgt))
    for nm,tgt in sheetfiles:
        if tgt not in z.namelist(): continue
        out.append(f'=== SHEET: {nm} ===')
        ws=ET.fromstring(z.read(tgt))
        for row in ws.iter():
            if strip_ns(row.tag)!='row': continue
            cells=[]
            for c in row:
                if strip_ns(c.tag)!='c': continue
                ref=c.get('r','')
                t=c.get('t')
                v=None
                for ch in c:
                    if strip_ns(ch.tag)=='v': v=ch.text
                    elif strip_ns(ch.tag)=='is':
                        v=''.join(x.text or '' for x in ch.iter() if strip_ns(x.tag)=='t')
                if v is None: continue
                if t=='s': v=shared[int(v)]
                col=re.sub(r'\d','',ref)
                cells.append(f'{col}={v}')
            if cells: out.append(' | '.join(cells))
    return '\n'.join(out)

def docx_dump(path):
    z=zipfile.ZipFile(path)
    out=[]
    for part in ['word/document.xml']:
        if part not in z.namelist(): continue
        r=ET.fromstring(z.read(part))
        for p in r.iter():
            if strip_ns(p.tag)=='p':
                txt=''.join(t.text or '' for t in p.iter() if strip_ns(t.tag)=='t')
                out.append(txt)
            elif strip_ns(p.tag)=='tbl':
                pass
        # tables: iterate rows
    # better: handle tables
    txt='\n'.join(out)
    return txt

def docx_full(path):
    z=zipfile.ZipFile(path)
    r=ET.fromstring(z.read('word/document.xml'))
    body=None
    for e in r: 
        if strip_ns(e.tag)=='body': body=e
    lines=[]
    def walk(el):
        tag=strip_ns(el.tag)
        if tag=='p':
            txt=''.join(t.text or '' for t in el.iter() if strip_ns(t.tag)=='t')
            lines.append(txt)
        elif tag=='tbl':
            for tr in el:
                if strip_ns(tr.tag)!='tr': continue
                cells=[]
                for tc in tr:
                    if strip_ns(tc.tag)!='tc': continue
                    ctxt=''.join(t.text or '' for t in tc.iter() if strip_ns(t.tag)=='t')
                    cells.append(ctxt)
                lines.append(' | '.join(cells))
        else:
            for c in el: walk(c)
    if body is not None:
        for c in body: walk(c)
    return '\n'.join(lines)

def pptx_dump(path):
    z=zipfile.ZipFile(path)
    out=[]
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n)],
                  key=lambda x:int(re.search(r'(\d+)',x.split('/')[-1]).group()))
    for s in slides:
        out.append(f'--- {s} ---')
        r=ET.fromstring(z.read(s))
        for t in r.iter():
            if strip_ns(t.tag)=='t':
                if t.text: out.append(t.text)
    return '\n'.join(out)

def pdf_dump(path):
    from PyPDF2 import PdfReader
    r=PdfReader(path)
    out=[]
    for i,pg in enumerate(r.pages):
        out.append(f'--- page {i+1} ---')
        out.append(pg.extract_text() or '')
    return '\n'.join(out)

f=sys.argv[1]
ext=f.rsplit('.',1)[-1].lower()
try:
    if ext=='xlsx': print(xlsx_dump(f))
    elif ext=='docx': print(docx_full(f))
    elif ext=='pptx': print(pptx_dump(f))
    elif ext=='pdf': print(pdf_dump(f))
    else:
        print(open(f,encoding='utf-8',errors='replace').read())
except Exception as e:
    print('ERROR',e)
