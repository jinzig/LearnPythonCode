# _*_ coding: utf-8 _*_
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

print('----------------SYSTEM LOADIUNG, please wait........')
SUMRESOURCES = 0 #全局变量
driver_detail = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver_item = webdriver.Firefox
url = "https://movie.douban.com/"
#等待页面家在方法
wait = ui.WebDriverWait(driver_item,15)
wait1 = ui.WebDriverWait(driver_detail, 15)

#获取url和文章标题
def getURL_Title():
    global SUMRESOURCES

# 需要输入获取信息，例 种类，排序，想看多少

    print('please select:')
    kind = input(
        "1-Hot\n2-Newest\n3-Classics\n4-Playable\n5-High Scores\n6-Wonderful but not popular\n7-Chinese film\n8-Hollywood\n9-Korea\n10-Japan\n11-Action movies\n12-Comedy\n13-Love story\n14-Science fiction\n15-Thriller\n16-Horror film\n17-Cartoon\nplease select:")
    print("-----------------------------------------------")
    sort = input("1-Sort by hot\n2-Sort by time\n2-Sort by score\nplease select:")
    print('----------------------------------------------')
    number = input("ToP?:")
    print('--------------------------')
    ask_long = input('dont need long comments, enter0, i like long commons enter 1:')
    print('-===-----------------------------')
    global save_name
    save_name = raw_input('save_name (xx.txt')
    print('-----------------crawling')
    driver_item.get(url)
    ##############################
    wait.until(
        lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]" % kind))
    driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]" % kind).click()
    wait.until(
        lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]" % sort))
    driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]" % sort).click()
    num = number + 1
    time.sleep(2)

    num_time = num/20+1
    wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list-wp']/a[@class='more']") )

    for times in range(1, num_time):
        time.sleep(1)
        driver_item.find_elements_by_xpath("//div[@class='list-wp']/a[@class='more']").click()
        time.sleep(1)
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]"%num))
    for i in range(1, num):
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]" % num))
        list_title = driver_item.find_element_by_xpath("//div[@class='list']/a[%d]" % i)
        print
        '----------------------------------------------' + 'NO' + str(
            SUMRESOURCES + 1) + '----------------------------------------------'
        print
        u'电影名: ' + list_title.text
        print
        u'链接: ' + list_title.get_attribute('href')  #unicode 转utf-8

        #写入txt部分1
        list_title_wr = list_title.text.encode('utf-8') #unicode码,需要重新编码再写入
