# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import common
import requests
from datetime import timedelta, datetime
import  os

userData = sys.argv[1]
executable_path = sys.argv[2]

class BusinessReport:
    #report(userData,executable_path)
    #send()

    def __init__(self, userData, executable_path):
        self.userData=userData
        self.executable_path=executable_path

    def report(self):
        yesterday = datetime.today() + timedelta(-1)
        yesterday_format = yesterday.strftime('%m-%d-%Y')
        driver = common.setDriver(self.userData,self.executable_path,r'D:\code\python')
        driver.get("https://sellercentral.amazon.com/gp/homepage.html")
        time.sleep(3)

        sign = driver.find_elements_by_css_selector(css_selector="#signInSubmit")
        if len(sign) > 0:
            driver.find_element_by_id("signInSubmit").click()

        driver.get("https://sellercentral.amazon.com/gp/site-metrics/report.html#&reportID=eD0RCS")
        time.sleep(5)
        driver.find_element_by_id("report_DetailSalesTrafficBySKU").click()
        time.sleep(5)

        js = "$('#fromDate2').val('"+yesterday_format+"');$('toDate2').val('"+yesterday_format+"');"
        driver.execute_script(js)

        driver.find_element_by_id("fromDate2").click()
        driver.find_element_by_xpath("//a[@class='ui-state-default ui-state-active']").click()

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='export']/span").click()
        driver.find_element_by_id("downloadCSV").click()


    def send(self):
        filesTmp=os.listdir(self.outFilePath)
        if len(filesTmp) >0:
            files = {'file': open(self.outFilePath+"/"+filesTmp[0], 'rb')}
            response = requests.post("http://localhost:8080/upload", files=files)


b=BusinessReport(userData,executable_path)
b.report()