# _*_ coding: utf-8 _*_
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random

#save as txt
def write2txt(data, path):
    f = open(path,"a")
    f.write(data)
    f.write("\n")
    f.close()

# get id music list
def catchSongs(url_id, url):
    user = url_id.split('=')[-1].strip()
    print('excute user:'), user

    driver = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx')
    driver.get(url)
    driver.switch_to_frame('g_iframe') #switch to frame
        try:
            songs = driver.find_element_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]'%song_key)
            info_ = songs[0.text.strip().split('\n')
            if len(info_) == 5:
                info_.insert(2, 'None') #no mv for this song
            new_line = '%s | %user+' '|'.join(info_)
            song_key +=1
            #new_line = '//*[@class="j-flag"]/table/tbody/tr[%s]'%song_key
            print(new_line)



