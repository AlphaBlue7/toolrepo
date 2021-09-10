import requests, hashlib
from bs4 import BeautifulSoup

url='http://138.68.155.238:30563/'

s=requests.session()
response=s.get(url)

soup= BeautifulSoup(response.content, "html.parser")
fin=soup.find('h3')
texx=fin.text
texx=texx.encode()

h=hashlib.md5()
h.update(texx)
ha=h.hexdigest()

print(s.post(url,data={'hash':ha}).text)