# _*_ coding: utf-8 _*_
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import select


def web_craw(url):
    driver = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get(url)
    comments = driver.find_element_by_xpath("//div[2]/div[2]/div/text()[2]")
    comment = comments.xpath('string(.)').extract()[0]
    for i in comments:
        type(i)
    type(comment)
        #print(i)


web_craw("http://www.dianping.com/shop/4667684/review_more?pageno=59")