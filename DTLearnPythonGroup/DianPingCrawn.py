# _*_ coding: utf-8 _*_
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import select


# def commnet_page_no(shopID):
#     driver = webdriver.Safari()
#     url = "http://www.dianping.com/shop/%s/review_more?pageno=1" % shopID
#     driver.get(url)
#
#
#     comments = driver.find_element_by_class_name("PageSel")
#     for i in comments:
#         i.text
#     print(type(comment))
#     print (i)
#     commpg = comments


def comments_wods(shopID, commpg):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # driver = webdriver.Chrome(chrome_options=options)
    pg = 1
    while pg <= commpg:
        driver = webdriver.Chrome(executable_path='/Users/sallyfan/downloads/chromedriver')
        # driver = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

        # driver = webdriver.Safari()
        url = "http://www.dianping.com/shop/%d/review_more?pageno=%d" % (shopID, pg)
        driver.get(url)
        pg +=1
        all_comments = []


        comments_content = driver.find_elements_by_class_name("J_brief-cont")
        with open('dianping.txt', 'w+') as f:
            for i in comments_content:
                # i.text
                print (i.text)
                f.write(i.text)



    # print (comments_content)

print(comments_wods(16795494, 72))