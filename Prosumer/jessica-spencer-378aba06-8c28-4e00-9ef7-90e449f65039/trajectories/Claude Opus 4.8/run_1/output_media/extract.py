import sys, zipfile, re, os
from xml.etree import ElementTree as ET

def docx_text(p):
    z=zipfile.ZipFile(p)
    out=[]
    for name in ['word/document.xml']:
        if name in z.namelist():
            xml=z.read(name).decode('utf-8','ignore')
            # paragraphs
            xml=xml.replace('</w:p>','\n')
            xml=re.sub(r'<w:tab[^>]*/>','\t',xml)
            txt=re.sub(r'<[^>]+>','',xml)
            out.append(txt)
    return '\n'.join(out)

def xlsx_text(p):
    z=zipfile.ZipFile(p)
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        x=z.read('xl/sharedStrings.xml').decode('utf-8','ignore')
        for m in re.findall(r'<si>(.*?)</si>', x, re.S):
            t=''.join(re.findall(r'<t[^>]*>(.*?)</t>', m, re.S))
            shared.append(re.sub(r'<[^>]+>','',t))
    out=[]
    # find sheets
    sheets=[n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml',n)]
    # try to map sheet names
    names={}
    if 'xl/workbook.xml' in z.namelist():
        wb=z.read('xl/workbook.xml').decode('utf-8','ignore')
        for i,m in enumerate(re.findall(r'<sheet[^>]*name="([^"]*)"',wb)):
            names[i]=m
    for si,sh in enumerate(sorted(sheets)):
        out.append(f'=== SHEET {si}: {names.get(si,sh)} ===')
        x=z.read(sh).decode('utf-8','ignore')
        for row in re.findall(r'<row[^>]*>(.*?)</row>', x, re.S):
            cells=[]
            for c in re.findall(r'<c[^>]*?(?:\s)?(?:t="([^"]*)")?[^>]*>(.*?)</c>', row, re.S):
                t,inner=c
                v=re.search(r'<v[^>]*>(.*?)</v>', inner, re.S)
                if v:
                    val=v.group(1)
                    if t=='s':
                        try: val=shared[int(val)]
                        except: pass
                    cells.append(val)
                else:
                    isv=re.search(r'<t[^>]*>(.*?)</t>', inner, re.S)
                    cells.append(isv.group(1) if isv else '')
            # also handle empty
            if cells:
                out.append('\t'.join(cells))
    return '\n'.join(out)

def pptx_text(p):
    z=zipfile.ZipFile(p)
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)],
                  key=lambda s:int(re.search(r'(\d+)',s).group(1)))
    out=[]
    for sl in slides:
        out.append(f'--- {sl} ---')
        x=z.read(sl).decode('utf-8','ignore')
        for t in re.findall(r'<a:t>(.*?)</a:t>', x, re.S):
            out.append(re.sub(r'<[^>]+>','',t))
    return '\n'.join(out)

def pdf_text(p):
    import PyPDF2
    r=PyPDF2.PdfReader(p)
    out=[]
    for i,pg in enumerate(r.pages):
        out.append(f'--- page {i+1} ---')
        try: out.append(pg.extract_text() or '')
        except Exception as e: out.append(f'[err {e}]')
    return '\n'.join(out)

f=sys.argv[1]
ext=f.lower().rsplit('.',1)[-1]
if ext=='docx': print(docx_text(f))
elif ext=='xlsx': print(xlsx_text(f))
elif ext=='pptx': print(pptx_text(f))
elif ext=='pdf': print(pdf_text(f))
else:
    print(open(f,encoding='utf-8',errors='ignore').read())
