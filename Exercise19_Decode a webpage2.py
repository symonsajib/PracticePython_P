


import requests
from bs4 import BeautifulSoup

#open the web site Vanity fair
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')
listH2 = soup.find_all('p')

for tag in listH2:
        print(tag.get_text())