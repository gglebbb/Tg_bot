import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as BS

country = input("Country:")
res=""
city = input("City:")
url = f"https://www/google.com/search&q={city}+{country}+what+time?+&start"
letters = "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю"

session = HTMLSession()
r = session.get(url)

html = BS(r.content, "lxml")
l = html.text.split(" ")
for i in range(len(l)):
    if "время" in l[i] and ":" in l[i]:
        s=l[i]
prom = list(s)
for i in range(len(prom)):
    if not(prom[i] in letters):
        res+=prom[i]
print(res)