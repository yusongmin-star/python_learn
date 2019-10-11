# coding:utf-8
from bs4 import BeautifulSoup
import requests
import re
import csv
import time

urls = []
company = []
areas1 = []
names = []
phoness = []
emails = []


class companyInfo():

    def get_company(self):
        r = requests.get('http://www.qiyetong.com/company_pr001003')

        # print(r.content)
        soup = BeautifulSoup(r.content, "html.parser")
        # print(soup)
        #list
        images = soup.find_all(class_="companyList")
        # print(images)
        images = str(images)
        #正则表达式规则
        pattern = '<a target="_blank" href="(.*?)" title="(.*?)">'
        #re.S作用：使用re.S参数以后，正则表达式会将这个字符串作为一个整体，而不只是单行匹配
        contents = re.findall(pattern, images)
        # print(contents)
        # 循环每页取urls，公司名称
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
            print(i)
            rr = requests.get(i)
            sp = BeautifulSoup(rr.content, "html.parser")
            # print(sp)
            phones = sp.find_all(class_='codl')
            # print(phones)
            phones = str(phones)
            #地区匹配
            pattern1 = '<li>经理：(.*?)</li>'
            area1 = re.findall(pattern1, phones, re.S)
            areas1.append(area1)
            # print(area1)
            #name匹配
            pattern3 = '<li>地址：(.*?)</li>'
            name = re.findall(pattern3, phones, re.S)
            names.append(name)
            # print(name)
            #手机号匹配
            pattern4 = '<li>手机：(.*?)</li>'
            phone = re.findall(pattern4, phones, re.S)
            phoness.append(phone)
            # print(phone)
            pattern5 = '<li>Email：(.*?)</li>'
            email = re.findall(pattern5, phones, re.S)
            emails.append(email)
        print(areas1)
        print(names)
        print(phoness)
        print(emails)
        csvfile = open("thirdly.csv", "wt", encoding='utf-8-sig')
        #csv多列写入定义
        writer = csv.writer(csvfile, delimiter=",")
        #定义标题
        header = ['company_name', 'address', 'contact_name', 'phone', 'email']
        writer.writerow(header)
        writer.writerows(zip(company, areas1, names, phoness, emails))



cm = companyInfo()
cm.get_company()
# cm.get_phone()


