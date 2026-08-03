import sys, zipfile, re, glob, os
from xml.etree import ElementTree as ET

def strip_ns(tag):
    return tag.split('}')[-1]

def docx_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        with z.open('word/document.xml') as f:
            data=f.read().decode('utf-8','ignore')
    # paragraphs
    for p in re.split(r'</w:p>', data):
        texts=re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S)
        line=''.join(texts)
        line=re.sub(r'<[^>]+>','',line)
        if line.strip():
            out.append(line)
    # tables handled by w:t already
    return '\n'.join(out)

def xlsx_text(path):
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            sdata=z.read('xl/sharedStrings.xml').decode('utf-8','ignore')
            for si in re.split(r'</si>', sdata):
                ts=re.findall(r'<t[^>]*>(.*?)</t>', si, re.S)
                if ts:
                    shared.append(re.sub(r'<[^>]+>','',''.join(ts)))
                elif '<si' in si:
                    shared.append('')
        sheets=[n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml', n)]
        result=[]
        for sh in sorted(sheets):
            result.append(f'--- {sh} ---')
            data=z.read(sh).decode('utf-8','ignore')
            for row in re.split(r'</row>', data):
                cells=[]
                for c in re.findall(r'<c[^>]*?(?:\s|>).*?(?:</c>|/>)', row, re.S):
                    ref=re.search(r'r="([A-Z]+\d+)"', c)
                    t=re.search(r't="([^"]+)"', c)
                    v=re.search(r'<v[^>]*>(.*?)</v>', c, re.S)
                    isv=re.search(r'<t[^>]*>(.*?)</t>', c, re.S)
                    val=''
                    if t and t.group(1)=='s' and v:
                        idx=int(v.group(1)); val=shared[idx] if idx<len(shared) else ''
                    elif isv:
                        val=re.sub(r'<[^>]+>','',isv.group(1))
                    elif v:
                        val=v.group(1)
                    if val!='':
                        cells.append(f'{ref.group(1) if ref else "?"}={val}')
                if cells:
                    result.append(' | '.join(cells))
        return '\n'.join(result)

def pptx_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml', n)],
                      key=lambda s:int(re.search(r'(\d+)',s).group(1)))
        for sl in slides:
            out.append(f'--- {sl} ---')
            data=z.read(sl).decode('utf-8','ignore')
            for p in re.split(r'</a:p>', data):
                ts=re.findall(r'<a:t>(.*?)</a:t>', p, re.S)
                line=re.sub(r'<[^>]+>','',''.join(ts))
                if line.strip():
                    out.append(line)
    return '\n'.join(out)

def main():
    for path in sys.argv[1:]:
        print('\n=================='+os.path.basename(path)+'==================')
        try:
            if path.endswith('.docx'): print(docx_text(path))
            elif path.endswith('.xlsx'): print(xlsx_text(path))
            elif path.endswith('.pptx'): print(pptx_text(path))
        except Exception as e:
            print('ERR',e)

main()
