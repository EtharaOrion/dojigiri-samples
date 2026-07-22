import sys, zipfile, re
from xml.etree import ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def col_to_idx(ref):
    m = re.match(r'([A-Z]+)(\d+)', ref)
    col = 0
    for c in m.group(1):
        col = col*26 + (ord(c)-64)
    return col-1, int(m.group(2))-1

def dump(path):
    z = zipfile.ZipFile(path)
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        root = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in root:
            txt = ''.join(t.text or '' for t in si.iter(NS+'t'))
            shared.append(txt)
    # find sheets
    wb = ET.fromstring(z.read('xl/workbook.xml'))
    rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    relmap = {r.get('Id'): r.get('Target') for r in rels}
    sheets = []
    for s in wb.iter(NS+'sheet'):
        rid = s.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        tgt = relmap.get(rid)
        if tgt and not tgt.startswith('/'):
            tgt = 'xl/'+tgt
        sheets.append((s.get('name'), tgt.lstrip('/')))
    for name, tgt in sheets:
        print(f'### SHEET: {name}')
        try:
            sroot = ET.fromstring(z.read(tgt))
        except KeyError:
            print('  (missing)'); continue
        for row in sroot.iter(NS+'row'):
            cells = {}
            maxc = 0
            for c in row.iter(NS+'c'):
                ref = c.get('r')
                ci, ri = col_to_idx(ref)
                t = c.get('t')
                v = c.find(NS+'v')
                is_ = c.find(NS+'is')
                if t == 's' and v is not None:
                    val = shared[int(v.text)]
                elif is_ is not None:
                    val = ''.join(x.text or '' for x in is_.iter(NS+'t'))
                elif v is not None:
                    val = v.text
                else:
                    val = ''
                cells[ci] = val
                maxc = max(maxc, ci)
            rowvals = [cells.get(i,'') for i in range(maxc+1)]
            print('\t'.join(rowvals))
        print()

for p in sys.argv[1:]:
    print(f'==================== {p} ====================')
    dump(p)
