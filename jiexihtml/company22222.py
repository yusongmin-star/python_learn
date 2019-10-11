# coding:utf-8
from bs4 import BeautifulSoup
import requests
import re
import csv

urls = []
company = []
areas1 = []
names = []
phoness = []

class companyInfo():

    def get_company(self):
        r = requests.get('http://m.qincai.net/iohohohoh/index.html')
        # print(r.content)
        soup = BeautifulSoup(r.content, "html.parser")
        # print(soup)
        #list
        images = soup.find_all(class_="itemlist")
        # print(images)
        images = str(images)
        #正则表达式规则
        pattern = '<a href="(.*?)" title="(.*?)">(\w*?)</a>'
        #re.S作用：使用re.S参数以后，正则表达式会将这个字符串作为一个整体，而不只是单行匹配
        contents = re.findall(pattern, images)
        # print(contents)
        #循环每页取urls，公司名称
        for content in contents:
            urls.append(content[0])
            # print(urls)
            company.append(content[1])
            # print(company)
        print(urls)
        print(company)

    def get_phone(self):
        #循环urls取公司的手机号等信息
        for i in urls:
            # print(i)
            rr = requests.get(i)
            sp = BeautifulSoup(rr.content, "html.parser")
            phones = sp.find_all(class_="contact-item")
            # print(phones)
            phones = str(phones)
            #地区匹配
            pattern1 = '<span class="contact-name">地址</span><span class="contact-value">(.*?)</span>'
            area1 = re.findall(pattern1, phones, re.S)
            areas1.append(area1)
            # print(area1)
            #name匹配
            pattern3 = '<span class="contact-name">联系人</span><span class="contact-value">(.*?)</span>'
            name = re.findall(pattern3, phones, re.S)
            names.append(name)
            # print(name)
            #手机号匹配
            pattern4 = '<span class="contact-name">电话</span><span class="contact-value">(.*?)</span>'
            phone = re.findall(pattern4, phones, re.S)
            phoness.append(phone)
            # print(phone)
        print(areas1)
        print(names)
        print(phoness)
        csvfile = open("second.csv", "wt", encoding='utf-8-sig')
        #csv多列写入定义
        writer = csv.writer(csvfile, delimiter=",")
        #定义标题
        header = ['company_name', 'address', 'contact_name', 'phone']
        writer.writerow(header)
        writer.writerows(zip(company, areas1, names, phoness))



cm = companyInfo()
cm.get_company()
cm.get_phone()

