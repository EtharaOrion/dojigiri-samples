import zipfile, xml.etree.ElementTree as ET, re, zlib, sys, os, html

def xlsx_to_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            root=ET.fromstring(z.read('xl/sharedStrings.xml'))
            ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
            for si in root.findall(ns+'si'):
                txt=''.join(t.text or '' for t in si.iter(ns+'t'))
                shared.append(txt)
        # sheet names
        names={}
        try:
            wb=ET.fromstring(z.read('xl/workbook.xml'))
            ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
            for i,sh in enumerate(wb.findall(ns+'sheets/'+ns+'sheet')):
                names[i+1]=sh.get('name')
        except Exception: pass
        sheets=sorted([n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml',n)])
        for si,s in enumerate(sheets):
            root=ET.fromstring(z.read(s))
            ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
            out.append('### SHEET: %s'%names.get(si+1,s))
            for row in root.iter(ns+'row'):
                cells=[]
                for c in row.findall(ns+'c'):
                    t=c.get('t'); v=c.find(ns+'v'); isv=c.find(ns+'is')
                    val=''
                    if t=='s' and v is not None:
                        val=shared[int(v.text)]
                    elif isv is not None:
                        val=''.join(x.text or '' for x in isv.iter(ns+'t'))
                    elif v is not None:
                        val=v.text or ''
                    cells.append(val)
                out.append('\t'.join(cells))
    return '\n'.join(out)

def docx_to_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name=='word/document.xml' or re.match(r'word/(header|footer)\d*\.xml',name):
                data=z.read(name)
                ns='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
                root=ET.fromstring(data)
                for p in root.iter(ns+'p'):
                    txt=''.join(t.text or '' for t in p.iter(ns+'t'))
                    # tables: also handle tabs
                    out.append(txt)
    return '\n'.join(out)

def pptx_to_text(path):
    out=[]
    with zipfile.ZipFile(path) as z:
        slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml',n)],
                      key=lambda x:int(re.search(r'(\d+)',x).group()))
        for s in slides:
            root=ET.fromstring(z.read(s))
            ns='{http://schemas.openxmlformats.org/drawingml/2006/main}'
            out.append('### %s'%s)
            for p in root.iter(ns+'p'):
                txt=''.join(t.text or '' for t in p.iter(ns+'t'))
                out.append(txt)
    return '\n'.join(out)

def pdf_to_text(path):
    import base64
    data=open(path,'rb').read()
    out=[]
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.S):
        raw=m.group(1).strip(b'\r\n')
        txt=None
        # try ascii85 then flate
        for attempt in ('a85+flate','flate','a85','raw'):
            try:
                d=raw
                if 'a85' in attempt:
                    d2=d.strip()
                    if d2.endswith(b'~>'): d2=d2[:-2]
                    d=base64.a85decode(d2, adobe=False)
                if 'flate' in attempt:
                    d=zlib.decompress(d)
                txt=d; break
            except Exception:
                continue
        if txt is None: txt=raw
        # extract text operators
        s=txt.decode('latin-1','ignore')
        # Tj: (....) Tj  ; TJ: [(..)..(..)] TJ
        for tm in re.finditer(r'\[(.*?)\]\s*TJ', s, re.S):
            parts=re.findall(r'\((?:[^()\\]|\\.)*\)', tm.group(1))
            line=''.join(re.sub(r'\\(.)',r'\1',p[1:-1]) for p in parts)
            if line.strip(): out.append(line)
        for tm in re.finditer(r'\((?:[^()\\]|\\.)*\)\s*Tj', s):
            p=re.search(r'\((.*)\)\s*Tj', tm.group(0), re.S).group(1)
            line=re.sub(r'\\(.)',r'\1',p)
            if line.strip(): out.append(line)
    return '\n'.join(out)

def html_to_text(path):
    s=open(path,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>','\t',s)
    s=html.unescape(s)
    s=re.sub(r'\n\s*\n','\n',s)
    return s

def any_to_text(path):
    ext=path.lower().rsplit('.',1)[-1]
    if ext=='xlsx': return xlsx_to_text(path)
    if ext=='docx': return docx_to_text(path)
    if ext=='pptx': return pptx_to_text(path)
    if ext=='pdf': return pdf_to_text(path)
    if ext in ('html','xml','tsv','csv','txt'): return open(path,encoding='utf-8',errors='ignore').read()
    return '[binary]'

if __name__=='__main__':
    os.makedirs('extract',exist_ok=True)
    for f in sorted(os.listdir('.')):
        if os.path.isdir(f) or f=='extract.py': continue
        ext=f.lower().rsplit('.',1)[-1] if '.' in f else ''
        if ext in ('mp3','mp4','jpg','png','gif','webp'): continue
        try:
            t=any_to_text(f)
            open('extract/'+f+'.txt','w').write(t)
            print('OK  %-14s %d chars'%(f,len(t)))
        except Exception as e:
            print('ERR %-14s %s'%(f,e))
