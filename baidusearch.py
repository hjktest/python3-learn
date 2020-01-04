# coding=utf-8
from selenium import  webdriver
import  time
import csv
import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#my_file='C:\\selenium\\data\\search.csv'
# values=csv.reader(file(my_file,'rb'))
values=csv.reader(open('C:\\selenium\\data\\search.csv','rb'))
for search in values:
    print (search[0])
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search[0])
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.quit()