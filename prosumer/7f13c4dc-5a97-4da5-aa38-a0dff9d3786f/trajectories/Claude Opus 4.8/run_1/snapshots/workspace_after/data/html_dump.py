import sys,re
from bs4 import BeautifulSoup
for p in sys.argv[1:]:
    print(f"\n########## {p} ##########")
    soup=BeautifulSoup(open(p,encoding='utf-8').read(),'html.parser')
    for t in soup(['script','style']): t.extract()
    # print tables in a structured way
    text=soup.get_text('\n')
    text=re.sub(r'\n\s*\n+','\n',text)
    print(text.strip())
