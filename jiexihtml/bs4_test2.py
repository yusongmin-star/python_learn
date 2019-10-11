# coding:utf-8
from bs4 import BeautifulSoup

chandao = open("chandao.html")
soup = BeautifulSoup(chandao,"html.parser")
tag = soup.a
print(soup.find_all("a"))  #打印所有的a标签
#获取class属性
print(tag["class"]) #默认匹配第一个a标签
print(tag.attrs) #获取a标签的所有属性
#获取文本属性
print(type(tag.string)) #这里Tag对象变成NavigableString对象了
print(tag.string)


