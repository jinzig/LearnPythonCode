# _*_ coding: utf-8 _*_
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import select





def comments_wods(shopID, commpg):
    uaList = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0']

    dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)

    dcap["phantomjs.page.settings.userAgent"] = (random.choice(uaList))

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
                all_comments.append(i.text)
            pg_comment= "".join(all_comments)
                # print (i.text)
            print(pg_comment)
    return pg_comment
            # f.write()

import jieba
wordlist = jieba.cut(comments_wods(), cut_all = True)
word_space_split = " ".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud

    # print (comments_content)

print(comments_wods(16795494, 72))