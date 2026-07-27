import sys,zlib,re
def decode_tj(arr):
    out=[]
    # tokens: <hex> or (string) or numbers
    i=0
    for m in re.finditer(rb'<([0-9A-Fa-f]*)>|\(((?:[^()\\]|\\.)*)\)|(-?\d+\.?\d*)',arr):
        if m.group(1) is not None:
            h=m.group(1)
            try: out.append(bytes.fromhex(h.decode()).decode('latin1'))
            except: pass
        elif m.group(2) is not None:
            s=re.sub(rb'\\([()\\])',rb'\1',m.group(2))
            out.append(s.decode('latin1'))
        else:
            num=float(m.group(3))
            if num< -60: out.append(' ')  # big negative kerning ~ space
    return ''.join(out)
def dump(path):
    data=open(path,'rb').read()
    texts=[]
    for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream',data,re.DOTALL):
        s=m.group(1)
        try: d=zlib.decompress(s)
        except:
            try: d=zlib.decompress(s.rstrip(b'\r\n'))
            except: d=s
        # each BT..ET block; also handle Td/Tm to add newlines
        for blk in re.finditer(rb'BT(.*?)ET',d,re.DOTALL):
            b=blk.group(1)
            line=''
            for tm in re.finditer(rb'\[(.*?)\]\s*TJ|\((.*?)\)\s*Tj',b,re.DOTALL):
                if tm.group(1) is not None:
                    line+=decode_tj(tm.group(1))
                elif tm.group(2) is not None:
                    line+=re.sub(rb'\\([()\\])',rb'\1',tm.group(2)).decode('latin1')
            if line.strip(): texts.append(line)
    return '\n'.join(texts)
for p in sys.argv[1:]:
    print(f"\n########## {p} ##########")
    try: print(dump(p))
    except Exception as e: print("ERR",e)
