from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
import common
import requests
from datetime import timedelta, datetime
import os



class Health:
    def __init__(self, userData, executable_path):
        self.userData = userData
        self.executable_path = executable_path
        self.outFilePath=r"D:\code\download\inventory_health"

    def report(self):
        yesterday = datetime.today() + timedelta(-1)
        yesterday_format = yesterday.strftime('%m-%d-%Y')
        driver= common.setDriver(self.userData,self.executable_path,self.outFilePath)
        driver.get("https://sellercentral.amazon.com/gp/homepage.html")
        time.sleep(3)

        sign = driver.find_elements_by_css_selector(css_selector="#signInSubmit")
        if len(sign) > 0:
            driver.find_element_by_id("signInSubmit").click()
		
        driver.get("https://sellercentral.amazon.com/gp/ssof/reports.html/ref=ag_fbareports_dnav_fbafulrpts_")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='sc-sidepanel']/div/ul[2]/li[22]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='INVENTORY_HEALTH']/a").click()
        time.sleep(3)
        driver.find_element_by_id("tab_download").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='downloadReportForm']/table/tbody/tr[4]/td[2]/button/span").click()
        time.sleep(200)
        driver.find_element_by_id("tab_download").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='downloadArchive']/table/tbody/tr[1]/td[4]/a/span/span").click()
        time.sleep(10)
    def send(self):
        filesTmp=os.listdir(self.outFilePath)
        if len(filesTmp) >0:
            files = {'file': open(self.outFilePath+"/"+filesTmp[0], 'rb')}
            response = requests.post("http://localhost:8080/upload", files=files)

