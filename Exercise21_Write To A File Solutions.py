from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nytimes.com/')
cont = page.content

soup = BeautifulSoup(cont, "html.parser")

for text in soup.find_all('p'):
    print(text.get_text() + '\n')

n = 0

with open('hello.txt', 'w') as open_file:
    for text in soup.find_all('p'):
        print(n)
        open_file.write(text.get_text() + '\n')
        n = n + 1
