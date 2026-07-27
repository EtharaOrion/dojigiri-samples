import sys,zlib,re
data=open(sys.argv[1],'rb').read()
out=[]
for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream',data,re.S):
    s=m.group(1)
    try:
        d=zlib.decompress(s)
    except Exception:
        d=s
    # extract text in parentheses from Tj/TJ
    for t in re.findall(rb'\((?:[^()\\]|\\.)*\)',d):
        txt=t[1:-1]
        txt=txt.replace(b'\\(',b'(').replace(b'\\)',b')').replace(b'\\\\',b'\\')
        out.append(txt.decode('latin-1'))
    # also BT..ET blocks with TJ arrays
print(' '.join(out))
# fallback: raw text if no streams
if not out:
    for t in re.findall(rb'\((?:[^()\\]|\\.)*\)',data):
        print(t[1:-1].decode('latin-1'))
