# coding:utf-8
from bs4 import BeautifulSoup

chandao = open("chandao.html")
soup = BeautifulSoup(chandao,"html.parser")
print(soup)
soup.prettify()
a = soup.find_all("div")
print(a)
print(len(a))




