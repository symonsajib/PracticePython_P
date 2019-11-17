from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nytimes.com/')
cont = page.content

soup = BeautifulSoup(cont, "html.parser")

list1 = soup.find_all(class_="esl82me1")

for i in list1:
    print(i.text)
    print(len(list1))
