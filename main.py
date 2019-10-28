from urllib.request import urlopen
from bs4 import BeautifulSoup

def sl(a):
    for i in range(128):
        if ord(a) == 38:
            return a
        if ord(a) == i:
            return ''
    return a

html = urlopen("http://www.gsm.hs.kr/main/main.php")  

bsObject = BeautifulSoup(html, "html.parser")
print(bsObject.dd)

l,iff,c,li = map(sl,str(bsObject.dd)),0,0,['']
for i in l:
    if i != '':
        iff = 1
        li[c] += i
    elif iff == 1:
        li.append('')
        iff=0
        c+=1

result = ''

for i in li:
    result += i+'\n'

r = "'''"+result+"'''"

print(r)