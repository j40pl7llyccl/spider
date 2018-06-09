from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import sys
import common
import requests
from datetime import timedelta, datetime
import os



class PerformanceByPlacement:
    def __init__(self, userData, executable_path):
        self.userData = userData
        self.executable_path = executable_path
        self.outFilePath=""

    def report(self):
        yesterday = datetime.today() + timedelta(-1)
        yesterday_format = yesterday.strftime('%m-%d-%Y')
        driver= common.setDriver(self.userData,self.executable_path,self.outFilePath)

        #driver.get("https://sellercentral.amazon.com/gp/homepage.html")
        #time.sleep(3)

        #sign = driver.find_elements_by_css_selector(css_selector="#signInSubmit")
        #if len(sign) > 0:
        #    driver.find_element_by_id("signInSubmit").click()
        
        driver.get("http://sahitest.com/demo/selectTest.htm")
        s1 = Select(driver.find_element_by_id('s1Id'))  #  instance of Select
        s1.select_by_visible_text("o3")
        time.sleep(10)
     
    def download(self):
        driver= common.setDriver(self.userData,self.executable_path,self.outFilePath)
        driver.get("https://sellercentral.amazon.com/gp/homepage.html")
        time.sleep(3)
        sign = driver.find_elements_by_css_selector(css_selector="#signInSubmit")
        if len(sign) > 0:
            driver.find_element_by_id("signInSubmit").click()

        driver.get("https://sellercentral.amazon.com/gp/advertiser/reports/sku-perf.html/ref=ag_xx_cont_perftime")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='DownloadID']/span").click()
        time.sleep(10)
    def send(self):
        filesTmp=os.listdir(self.outFilePath)
        if len(filesTmp) >0:
            files = {'file': open(self.outFilePath+"/"+filesTmp[0], 'rb')}
            response = requests.post("http://localhost:8080/upload", files=files)