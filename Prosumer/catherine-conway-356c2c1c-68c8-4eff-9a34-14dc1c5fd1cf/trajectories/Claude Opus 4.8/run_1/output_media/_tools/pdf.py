#!/usr/bin/env python3
import sys, re, zlib, base64

def a85(data):
    data = data.strip()
    if data.startswith(b'<~'): data = data[2:]
    if data.endswith(b'~>'): data = data[:-2]
    return base64.a85decode(data, adobe=False)

def decode_stream(dictpart, raw):
    filters = re.findall(rb'/(ASCII85Decode|FlateDecode|ASCIIHexDecode)', dictpart)
    d = raw
    for f in filters:
        if f == b'ASCII85Decode':
            d = a85(d)
        elif f == b'FlateDecode':
            d = zlib.decompress(d)
        elif f == b'ASCIIHexDecode':
            h = re.sub(rb'\s','',d).rstrip(b'>')
            d = bytes.fromhex(h.decode())
    return d

def extract(path):
    data = open(path,'rb').read()
    out = []
    for m in re.finditer(rb'(<<[^>]*?/Length[^>]*?>>)\s*stream\r?\n(.*?)\r?\nendstream', data, re.S):
        dictpart, raw = m.group(1), m.group(2)
        try:
            dec = decode_stream(dictpart, raw)
        except Exception as e:
            continue
        out.append(parse_text(dec))
    return '\n'.join(x for x in out if x.strip())

def parse_text(dec):
    chunks = []
    # Tj strings
    for tm in re.finditer(rb'\((?:[^()\\]|\\.)*\)\s*Tj', dec, re.S):
        inner = re.match(rb'\((.*)\)\s*Tj', tm.group(0), re.S).group(1)
        chunks.append(unescape(inner))
    # TJ arrays
    for tm in re.finditer(rb'\[(.*?)\]\s*TJ', dec, re.S):
        parts = re.findall(rb'\((?:[^()\\]|\\.)*\)', tm.group(1))
        s = b''.join(re.match(rb'\((.*)\)', p, re.S).group(1) for p in parts)
        chunks.append(unescape(s))
    return ' '.join(c.decode('latin-1','replace') for c in chunks)

def unescape(b):
    b = b.replace(rb'\(', b'(').replace(rb'\)', b')')
    b = b.replace(rb'\n', b'\n').replace(rb'\r', b'\r').replace(rb'\t', b'\t').replace(rb'\\', b'\\')
    return b

if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('\n########## PDF: %s ##########' % p)
        try:
            print(extract(p))
        except Exception as e:
            print('ERR', e)
