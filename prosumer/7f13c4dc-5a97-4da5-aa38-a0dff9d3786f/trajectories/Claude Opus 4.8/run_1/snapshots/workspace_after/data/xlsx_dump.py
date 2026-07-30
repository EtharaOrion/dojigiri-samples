import sys, zipfile, re
from xml.etree import ElementTree as ET
NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
def col_to_num(c):
    n=0
    for ch in c:
        if ch.isalpha(): n=n*26+(ord(ch.upper())-64)
    return n
def dump(path):
    z=zipfile.ZipFile(path)
    shared=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        r=ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in r.findall(NS+'si'):
            shared.append(''.join(t.text or '' for t in si.iter(NS+'t')))
    # sheet names
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    names=[s.get('name') for s in wb.iter(NS+'sheet')]
    sheets=sorted([n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml',n)])
    for idx,sp in enumerate(sheets):
        nm=names[idx] if idx<len(names) else sp
        print(f"=== SHEET: {nm} ({sp}) ===")
        r=ET.fromstring(z.read(sp))
        for row in r.iter(NS+'row'):
            cells=[]
            for c in row.findall(NS+'c'):
                ref=c.get('r'); t=c.get('t')
                v=c.find(NS+'v'); isv=c.find(NS+'is')
                val=''
                if t=='s' and v is not None: val=shared[int(v.text)]
                elif t=='inlineStr' and isv is not None: val=''.join(x.text or '' for x in isv.iter(NS+'t'))
                elif v is not None: val=v.text
                col=re.match(r'[A-Z]+',ref).group()
                cells.append(f"{col}={val}")
            if cells: print(' | '.join(cells))
        print()
for p in sys.argv[1:]:
    print(f"\n########## FILE {p} ##########")
    try: dump(p)
    except Exception as e: print("ERR",e)
