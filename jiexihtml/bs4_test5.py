# coding:utf-8
from bs4 import BeautifulSoup
import requests
r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
# print(r.content)
soup = BeautifulSoup(r.content, "html.parser")
#list
images = soup.find_all(class_="lazy")
#print(images)
urls = []
for i in images:
    url = i["data-original"]
    # title = i["title"]
    # print(url)
    # print(title)
    urls.append(url)
    # ima = requests.get(url)
    # with open(title+".jpg","wb") as f:
    #     f.write(ima.content)
print(urls)
with open("xx.txt", "w") as f:
    f.write("\n".join(urls))
