import sys, zipfile, zlib, re, os

def pdf_text(path):
    data = open(path,'rb').read()
    out=[]
    for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream', data, re.S):
        s=m.group(1)
        try:
            d=zlib.decompress(s)
        except Exception:
            d=s
        # extract text in parentheses from Tj/TJ
        txt=[]
        for tm in re.finditer(rb'\((?:[^()\\]|\\.)*\)', d):
            seg=tm.group(0)[1:-1]
            seg=seg.replace(b'\\(',b'(').replace(b'\\)',b')').replace(b'\\\\',b'\\')
            txt.append(seg.decode('latin-1'))
        if txt:
            out.append(''.join(txt))
    return '\n'.join(out)

def docx_text(path):
    z=zipfile.ZipFile(path)
    xml=z.read('word/document.xml').decode('utf-8','replace')
    xml=xml.replace('</w:p>','\n').replace('</w:tr>','\n').replace('</w:tc>','\t')
    xml=re.sub(r'<[^>]+>','',xml)
    import html
    return html.unescape(xml)

def xlsx_text(path):
    z=zipfile.ZipFile(path)
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        ss=z.read('xl/sharedStrings.xml').decode('utf-8','replace')
        for m in re.finditer(r'<si>(.*?)</si>', ss, re.S):
            t=''.join(re.findall(r'<t[^>]*>(.*?)</t>', m.group(1), re.S))
            import html
            shared.append(html.unescape(t))
    out=[]
    sheets=[n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml', n)]
    for sh in sorted(sheets):
        out.append('### '+sh)
        xml=z.read(sh).decode('utf-8','replace')
        for row in re.finditer(r'<row[^>]*>(.*?)</row>', xml, re.S):
            cells=[]
            for c in re.finditer(r'<c[^>]*?(?:\st="(\w+)")?[^>]*>(?:<v>(.*?)</v>|<is><t[^>]*>(.*?)</t></is>)?</c>', row.group(1), re.S):
                typ=c.group(1); v=c.group(2); istr=c.group(3)
                if istr is not None:
                    cells.append(istr)
                elif v is not None:
                    if typ=='s':
                        cells.append(shared[int(v)])
                    else:
                        cells.append(v)
                else:
                    cells.append('')
            out.append('\t'.join(cells))
    import html
    return html.unescape('\n'.join(out))

def pptx_text(path):
    z=zipfile.ZipFile(path)
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)], key=lambda x:int(re.findall(r'\d+',x)[0]))
    out=[]
    import html
    for s in slides:
        out.append('--- '+s+' ---')
        xml=z.read(s).decode('utf-8','replace')
        for m in re.finditer(r'<a:t>(.*?)</a:t>', xml, re.S):
            out.append(html.unescape(m.group(1)))
    return '\n'.join(out)

path=sys.argv[1]
ext=path.rsplit('.',1)[-1].lower()
if ext=='pdf': print(pdf_text(path))
elif ext=='docx': print(docx_text(path))
elif ext=='xlsx': print(xlsx_text(path))
elif ext=='pptx': print(pptx_text(path))
else: print(open(path).read())
