import csv
import os


def main():
    csvfile = open("csss.csv", 'wt' ,encoding="UTF8")  #

    writer=csv.writer(csvfile, delimiter=",")
    header=['uel','title']
    csvrow1=[]
    csvrow2=[]
    csvrow1.append("测试1")
    csvrow1.append("测试2")
    csvrow2.append("111")
    csvrow2.append("222")

    writer.writerow(header)
    writer.writerows(zip(csvrow1,csvrow2))


    csvfile.close()

if __name__ == '__main__':
    main()
