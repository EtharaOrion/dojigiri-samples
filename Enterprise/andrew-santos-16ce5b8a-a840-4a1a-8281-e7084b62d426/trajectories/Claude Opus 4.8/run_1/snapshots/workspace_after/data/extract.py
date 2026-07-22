import zipfile, re, sys, glob, os
from xml.etree import ElementTree as ET

def docx_text(p):
    z=zipfile.ZipFile(p)
    xml=z.read('word/document.xml').decode('utf-8',errors='replace')
    # paragraphs
    xml=xml.replace('</w:p>','\n')
    xml=xml.replace('</w:tr>','\n')
    xml=re.sub(r'<w:tab[^>]*/>','\t',xml)
    txt=re.sub(r'<[^>]+>','',xml)
    import html
    return html.unescape(txt)

def xlsx_text(p):
    z=zipfile.ZipFile(p)
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        s=z.read('xl/sharedStrings.xml').decode('utf-8',errors='replace')
        for m in re.findall(r'<si>(.*?)</si>',s,re.S):
            t=''.join(re.findall(r'<t[^>]*>(.*?)</t>',m,re.S))
            import html
            shared.append(html.unescape(re.sub(r'<[^>]+>','',t)))
    out=[]
    sheets=sorted([n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml',n)])
    for sh in sheets:
        out.append(f'=== {sh} ===')
        data=z.read(sh).decode('utf-8',errors='replace')
        for row in re.findall(r'<row[^>]*>(.*?)</row>',data,re.S):
            cells=[]
            for c in re.findall(r'<c[^>]*?(?:\s+t="([^"]*)")?[^>]*>(.*?)</c>',row,re.S):
                typ,body=c
                v=re.findall(r'<v[^>]*>(.*?)</v>',body,re.S)
                inl=re.findall(r'<t[^>]*>(.*?)</t>',body,re.S)
                if typ=='s' and v:
                    cells.append(shared[int(v[0])] if int(v[0])<len(shared) else '')
                elif inl:
                    import html
                    cells.append(html.unescape(''.join(inl)))
                elif v:
                    cells.append(v[0])
                else:
                    cells.append('')
            out.append('\t'.join(cells))
    return '\n'.join(out)

def pptx_text(p):
    z=zipfile.ZipFile(p)
    out=[]
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)],
                  key=lambda x:int(re.findall(r'\d+',x)[0]))
    import html
    for sl in slides:
        out.append(f'--- {sl} ---')
        d=z.read(sl).decode('utf-8',errors='replace')
        d=d.replace('</a:p>','\n')
        for t in re.findall(r'<a:t>(.*?)</a:t>',d,re.S):
            pass
        txt=re.sub(r'<[^>]+>','',d)
        out.append(html.unescape(txt))
    return '\n'.join(out)

f=sys.argv[1]
ext=f.rsplit('.',1)[-1].lower()
if ext=='docx': print(docx_text(f))
elif ext=='xlsx': print(xlsx_text(f))
elif ext=='pptx': print(pptx_text(f))
