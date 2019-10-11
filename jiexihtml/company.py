# coding:utf-8
from bs4 import BeautifulSoup
import requests
import re
import csv

urls = []
company = []
areas1 = []
areas2 = []
QQs = []
phoness = []


class companyInfo():

    def get_company(self):
        #循环公司页数
        for i in range(51):
            r = requests.get('https://www.bestb2b.com/companys_'+str(i)+'.htm')
            print(i)
            # print(r.content)
            soup = BeautifulSoup(r.content, "html.parser")
            # print(soup)
            #list
            images = soup.find_all(class_="listInfo")
            # print(images)
            images = str(images)
            #正则表达式规则
            pattern = '<a href="(.*?)" target="_blank">(\w*?)</a>'
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
            rr = requests.get('https://www.bestb2b.com'+i)
            sp = BeautifulSoup(rr.content, "html.parser")
            phones = sp.find_all(id="viewAttribute")
            # print(phones)
            phones = str(phones)
            #地区匹配
            pattern1 = '<td class="att" width="40">国家地区</td><td valign="top" width="200">(.*?)</td>'
            area1 = re.findall(pattern1, phones, re.S)
            areas1.append(area1)
            # print(area1)
            #地址匹配
            pattern2 = '</td></tr> <tr><td class="att">地址</td><td valign="top">(.*?)</td>'
            area2 = re.findall(pattern2, phones, re.S)
            areas2.append(area2)
            # print(area2)
            #QQ匹配
            pattern3 = '<td class="att">QQ</td>(.*?)<td valign="top"(.*?)</td>'
            QQ = re.findall(pattern3, phones, re.S)
            QQs.append(QQ)
            # print(QQ)
            #手机号匹配
            pattern4 = '<td class="att">手机</td><td valign="top">(.*?)</td>'
            phone = re.findall(pattern4, phones, re.S)
            phoness.append(phone)
            # print(phone)
        print(areas1)
        print(areas2)
        print(QQs)
        print(phoness)


        csvfile = open("companys.csv", "wt", encoding='utf-8-sig')
        #csv多列写入定义
        writer = csv.writer(csvfile, delimiter=",")
        #定义标题
        header = ['company_name', 'city', 'address', 'qq', 'phone']
        writer.writerow(header)
        writer.writerows(zip(company, areas1, areas2, QQs, phoness))

cm = companyInfo()
cm.get_company()
cm.get_phone()