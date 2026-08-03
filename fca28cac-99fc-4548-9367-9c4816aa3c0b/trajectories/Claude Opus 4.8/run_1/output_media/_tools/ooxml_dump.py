import sys, zipfile, re
from xml.etree import ElementTree as ET

def dump_docx(z):
    xml=z.read('word/document.xml').decode('utf-8')
    # paragraphs
    for p in re.split(r'</w:p>', xml):
        txts=re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S)
        line=''.join(txts)
        line=re.sub(r'&amp;','&',line); line=re.sub(r'&lt;','<',line); line=re.sub(r'&gt;','>',line)
        if line.strip(): print(line)

def dump_pptx(z):
    names=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n)],
                 key=lambda x:int(re.search(r'(\d+)',x).group(1)))
    for n in names:
        print(f'----- {n} -----')
        xml=z.read(n).decode('utf-8')
        for t in re.findall(r'<a:t>(.*?)</a:t>', xml, re.S):
            t=re.sub(r'&amp;','&',t)
            print(t)

for p in sys.argv[1:]:
    print(f'==================== {p} ====================')
    z=zipfile.ZipFile(p)
    if 'word/document.xml' in z.namelist(): dump_docx(z)
    else: dump_pptx(z)
