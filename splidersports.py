import requests
import re
from bs4 import BeautifulSoup

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
headers={"User-Agent":user_agent}

res = requests.get("http://sports.sina.com.cn/",headers=headers)
res.encoding = "utf-8"
html =res.text

list=[]
fout1=open("sports.txt","a",encoding="utf-8")

soup = BeautifulSoup(html, 'lxml')
divstylea=soup.find_all("a",attrs={"href":re.compile("^http://sports.sina.com.cn/")})
divstyle=set(divstylea)
for div in divstyle:
    list.append(div.get("href"))
    print(div.get("href"))
print(len(divstyle))


for k in list:
    res = requests.get(k, headers=headers)
    res.encoding = "utf-8"
    html = res.text
    soupnew = BeautifulSoup(html, 'lxml')
    div = soupnew.find("div", id="artibody")
    if div is None:
        continue
    p = div.find_all("p")
    str = ""
    for j in p:
        # str=""
        str += j.get_text().strip()
    str+="\n"
    print(str)
    fout1.write(str)
fout1.close()



