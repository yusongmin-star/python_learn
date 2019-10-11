# coding:utf-8
from bs4 import BeautifulSoup

chandao = open("chandao.html")
soup = BeautifulSoup(chandao,"html.parser")
print(soup)\

print(type(soup)) #整个
# soup.prettify()

print(soup.title)  #Tag
print(type(soup.title))

print(soup.title.string)  #string
print(type(soup.title.string))

