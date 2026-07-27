import sys,zipfile,re
from xml.etree import ElementTree as ET
def docx(path):
    z=zipfile.ZipFile(path); xml=z.read('word/document.xml').decode('utf-8')
    xml=re.sub(r'</w:p>','\n',xml); xml=re.sub(r'<w:tab/>','\t',xml)
    txt=re.sub(r'<[^>]+>','',xml)
    import html; return html.unescape(txt)
def pptx(path):
    z=zipfile.ZipFile(path)
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)],
                  key=lambda s:int(re.search(r'\d+',s.split('/')[-1]).group()))
    out=[]
    for s in slides:
        xml=z.read(s).decode('utf-8')
        xml=re.sub(r'</a:p>','\n',xml)
        txt=re.sub(r'<[^>]+>','',xml)
        import html
        out.append(f"--- {s} ---\n"+html.unescape(txt))
    return '\n'.join(out)
for p in sys.argv[1:]:
    print(f"\n########## {p} ##########")
    try:
        print(docx(p) if p.endswith('.docx') else pptx(p))
    except Exception as e: print("ERR",e)
