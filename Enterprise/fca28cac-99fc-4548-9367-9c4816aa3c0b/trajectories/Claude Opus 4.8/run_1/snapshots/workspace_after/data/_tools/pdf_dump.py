import sys, zlib, re, binascii

def decode_tj_operand(op):
    # op is content of [...] or a (..)/<..> string
    out=[]
    for m in re.finditer(r'<([0-9A-Fa-f\s]*)>|\(((?:[^()\\]|\\.)*)\)', op):
        if m.group(1) is not None:
            h=re.sub(r'\s','',m.group(1))
            if len(h)%2: h=h[:-1]
            try: out.append(binascii.unhexlify(h).decode('latin1'))
            except: pass
        else:
            s=m.group(2)
            s=re.sub(r'\\([()\\])',r'\1',s)
            out.append(s)
    return ''.join(out)

def extract(path):
    data=open(path,'rb').read()
    streams=re.findall(rb'stream\r?\n(.*?)endstream',data,re.S)
    lines=[]
    for s in streams:
        s=s.rstrip(b'\r\n')
        try: d=zlib.decompress(s).decode('latin1')
        except:
            try: d=s.decode('latin1')
            except: continue
        cur=''
        last_y=None
        for tok in re.finditer(r'BT(.*?)ET', d, re.S):
            block=tok.group(1)
            # get Y position
            ym=re.search(r'1 0 0 1 [\d.\-]+ ([\d.\-]+) Tm', block)
            txt=''
            for tj in re.finditer(r'\[(.*?)\]\s*TJ|((?:<[0-9A-Fa-f\s]*>|\((?:[^()\\]|\\.)*\)))\s*Tj', block, re.S):
                operand=tj.group(1) if tj.group(1) is not None else tj.group(2)
                txt+=decode_tj_operand(operand)
            lines.append(txt)
    print('\n'.join(lines))

for p in sys.argv[1:]:
    print(f'==================== {p} ====================')
    try: extract(p)
    except Exception as e: print('ERR',e)
