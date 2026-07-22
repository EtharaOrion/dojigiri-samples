import sys, re, zlib, os

def extract(path):
    data=open(path,'rb').read()
    texts=[]
    # find streams
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', data, re.S):
        raw=m.group(1)
        raw=raw.strip(b'\r\n')
        try:
            dec=zlib.decompress(raw)
        except Exception:
            dec=raw
        # extract text in parentheses from BT/ET or Tj/TJ
        for tm in re.finditer(rb'\((?:[^()\\]|\\.)*\)', dec):
            s=tm.group(0)[1:-1]
            s=s.replace(b'\\(',b'(').replace(b'\\)',b')').replace(b'\\\\',b'\\')
            texts.append(s.decode('latin-1'))
        # TJ arrays
    return texts

for p in sys.argv[1:]:
    print('\n=========='+os.path.basename(p)+'==========')
    t=extract(p)
    print(' '.join(t))
