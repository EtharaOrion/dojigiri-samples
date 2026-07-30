#!/usr/bin/env python3
import sys, zipfile, re, zlib, csv, io, html, xml.etree.ElementTree as ET

def strip_ns(tag):
    return tag.split('}')[-1]

def xlsx_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            root=ET.fromstring(z.read('xl/sharedStrings.xml'))
            for si in root:
                txt=''.join(t.text or '' for t in si.iter() if strip_ns(t.tag)=='t')
                shared.append(txt)
        # sheet order
        sheets=[n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml',n)]
        sheets.sort(key=lambda n:int(re.search(r'sheet(\d+)',n).group(1)))
        for sh in sheets:
            out.append(f"=== {sh} ===")
            root=ET.fromstring(z.read(sh))
            for row in root.iter():
                if strip_ns(row.tag)!='row': continue
                cells=[]
                for c in row:
                    if strip_ns(c.tag)!='c': continue
                    t=c.get('t')
                    v=None
                    for ch in c:
                        if strip_ns(ch.tag)=='v': v=ch.text
                        if strip_ns(ch.tag)=='is':
                            v=''.join(x.text or '' for x in ch.iter() if strip_ns(x.tag)=='t')
                    if v is None: 
                        cells.append('')
                        continue
                    if t=='s':
                        cells.append(shared[int(v)])
                    else:
                        cells.append(v)
                out.append('\t'.join(cells))
    return '\n'.join(out)

def docx_text(path):
    with zipfile.ZipFile(path) as z:
        parts=[n for n in z.namelist() if n=='word/document.xml' or re.match(r'word/(header|footer)\d*\.xml',n)]
        out=[]
        for p in parts:
            root=ET.fromstring(z.read(p))
            for para in root.iter():
                if strip_ns(para.tag)=='p':
                    txt=''.join(t.text or '' for t in para.iter() if strip_ns(t.tag)=='t')
                    out.append(txt)
                if strip_ns(para.tag)=='tbl':
                    pass
        return '\n'.join(out)

def pptx_text(path):
    with zipfile.ZipFile(path) as z:
        slides=[n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)]
        slides.sort(key=lambda n:int(re.search(r'slide(\d+)',n).group(1)))
        out=[]
        for s in slides:
            out.append(f"=== {s} ===")
            root=ET.fromstring(z.read(s))
            for t in root.iter():
                if strip_ns(t.tag)=='t':
                    out.append(t.text or '')
        return '\n'.join(out)

def html_text(path):
    data=open(path,encoding='utf-8',errors='replace').read()
    data=re.sub(r'<script.*?</script>','',data,flags=re.S)
    data=re.sub(r'<style.*?</style>','',data,flags=re.S)
    data=re.sub(r'<[^>]+>',' ',data)
    return html.unescape(re.sub(r'[ \t]+',' ',data))

def pdf_text(path):
    import base64
    data=open(path,'rb').read()
    out=[]
    for m in re.finditer(rb'stream\r?\n', data):
        start=m.end()
        end=data.find(b'endstream',start)
        raw=data[start:end].rstrip(b'\r\n')
        # find preceding dict for filters
        head=data[max(0,m.start()-300):m.start()]
        filters=re.findall(rb'/(ASCII85Decode|FlateDecode|LZWDecode|ASCIIHexDecode)',head)
        dec=raw
        try:
            for f in filters:
                if f==b'ASCII85Decode':
                    s=dec.strip()
                    if s.endswith(b'~>'): s=s[:-2]
                    dec=base64.a85decode(s)
                elif f==b'FlateDecode':
                    dec=zlib.decompress(dec)
                elif f==b'ASCIIHexDecode':
                    s=dec.strip().rstrip(b'>')
                    dec=bytes.fromhex(s.decode('latin-1').replace('\n','').replace(' ',''))
            if not filters:
                dec=zlib.decompress(raw)
        except Exception:
            try: dec=zlib.decompress(raw)
            except Exception: dec=raw
        # extract text ops
        txt=[]
        for tm in re.finditer(rb'\((?:[^()\\]|\\.)*\)|\[(?:[^\]])*\]', dec):
            s=tm.group(0)
            # handle TJ arrays and Tj strings
            for sm in re.finditer(rb'\((?:[^()\\]|\\.)*\)', s):
                inner=sm.group(0)[1:-1]
                inner=inner.replace(b'\\(',b'(').replace(b'\\)',b')').replace(b'\\\\',b'\\')
                txt.append(inner.decode('latin-1'))
        joined=''.join(txt)
        if joined.strip():
            out.append(joined)
    return '\n'.join(out)

def main():
    path=sys.argv[1]
    low=path.lower()
    if low.endswith('.xlsx'): print(xlsx_text(path))
    elif low.endswith('.docx'): print(docx_text(path))
    elif low.endswith('.pptx'): print(pptx_text(path))
    elif low.endswith('.html'): print(html_text(path))
    elif low.endswith(('.tsv','.csv','.xml','.txt')): print(open(path,encoding='utf-8',errors='replace').read())
    elif low.endswith('.pdf'): print(pdf_text(path))
    else: print('unsupported',path)

if __name__=='__main__':
    main()
