# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os



def setDriver(userData,executable_path,outFilePath):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + userData)
    prefs = {'profile.default_content_settings.popups': 0,
             'download.default_directory': outFilePath}
    options.add_experimental_option('prefs', prefs)
    executable_path = executable_path
    driver = webdriver.Chrome(executable_path, chrome_options=options)
    return driver