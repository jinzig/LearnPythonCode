from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from Tkinter import *


print('system loading, please wait o ...')
#  获取电影名及url
def getURL_Title():
    global save_name
    SUMRESOURES = 0
    url = 'https://movie.douban.com'
    driver_item = webdriver.Firefox()
    wait = ui.WebDriverWait(driver_item, 15)

