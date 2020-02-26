# coding=utf-8
from selenium import  webdriver
import  time
import csv
import pandas as pd
# import file
import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
# my_file='C:\\selenium\\data\\search.csv'
# values=csv.reader('my_file','rb')
# values=csv.reader(open('C:\\selenium\\data\\search.csv','rb'))
# print(values)
# with open('C:\\selenium\\data\\search.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     column1 = [row[2] for row in reader]
#     print(column1)
#     # d = pd.read_csv('C:\\selenium\\data\\search.csv', usecols=[])
#     # print(d)
column1=['hou','ggh']
for search in column1:
    print (search)
    # driver = webdriver.Chrome()
    # driver.get("https://www.baidu.com")
    # driver.find_element_by_id("kw").send_keys(search)
    # driver.find_element_by_id("su").click()
    # time.sleep(3)
    # driver.quit()
a=(1,2,3,4)
print(a)
