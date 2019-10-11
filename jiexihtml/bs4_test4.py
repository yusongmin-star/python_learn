#coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.cnblogs.com/yoyoketang/?_wv=1031")
# print(r.content)

soup = BeautifulSoup(r.content,"html.parser")
images = soup.find_all(class_="forFlow") #list
div = images[0].find_all(class_="postTitle2")
print(div)
print(len(div))
for i in  div:
    print(i.get_text())
    # print(i.string)

