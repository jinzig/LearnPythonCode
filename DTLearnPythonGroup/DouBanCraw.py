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
    save_name = input('save_name (xx.txt)')
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
        list_title_wr = list_title.text.encode('utf-8') #unicode码,需要重新编码再写入txt
        list_title_url_wr = list_title.get_attribute('href')

        Write_txt('\n----------------------------------------------' + 'NO' + str(
            SUMRESOURCES + 1) + '----------------------------------------------', '', save_name)
        Write_txt(list_title_wr, list_title_url_wr, save_name)

        SUMRESOURCES = SUMRESOURCES +1

        try: #get conmment , herf is link url
            getDetails(str(list_title.get_attribute('href')),ask_long)
        except:
            print('can not get the details!')

######
#当选择一部电影后，进入这部电影的超链接，然后才能获取
#同时别忽视元素加载的问题
#在加载长评论的时候，注意模拟点击一次小三角，不然可能会使内容隐藏
##########################################################

def getDetails(url, ask_long):
    driver_detail.get(url)
    wait1.until(lambda driver: driver.find_element_by_xpath("//div[@id='link-report']/span"))
    drama = driver_detail.find_elements_by_xpath("//div[@id='link-report']/span")
    print(u"剧情简介："+ drama.text)
    drama_wr = drama.text.encode('utf-8')
    Write_txt(drama_wr, '',save_name)
    print("------------------hot comments top------------")
    for i in range(1,5):
        try:
            comments_hot = driver_detail.find_element_by_xpath("//div[@id='hot-comments']/div[%s]/div/p"%i)
            print(u"最新热评：" + comments_hot.text)
            comments_hot_wr = comments_hot.text.encode('utf-8')
            Write_txt("------------------hot comments top%d-----------------------------------------------"%i,'',save_name)
            Write_txt(comments_hot_wr,'',save_name)
        except:
            print( 'can not caught the comments!')
            # 加载长评
        if ask_long == 1:
            try:
                driver_detail.find_element_by_xpath("//img[@class='bn-arrow']").click()
                # wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='review-bd']/div[2]/div/div"))
                time.sleep(1)
                # 解决加载长评会提示剧透问题导致无法加载
                comments_get = driver_detail.find_element_by_xpath("//div[@class='review-bd']/div[2]/div")
                if comments_get.text.encode('utf-8') == '提示: 这篇影评可能有剧透':
                    comments_deep = driver_detail.find_element_by_xpath("//div[@class='review-bd']/div[2]/div[2]")
                else:
                    comments_deep = comments_get
                print(
                "--------------------------------------------long-comments---------------------------------------------")
                print(
                u"深度长评：" + comments_deep.text)
                comments_deep_wr = comments_deep.text.encode('utf-8')
                Write_txt(
                    "--------------------------------------------long-comments---------------------------------------------\n",
                    '', save_name)
                Write_txt(comments_deep_wr, '', save_name)
            except:
                print
                ('can not caught the deep_comments!')
##############################################################################
#将print输出的写入txt中查看，也可以在cmd中查看，换行符是为了美观
##############################################################################
def Write_txt(text1='',text2='',title='douban.txt'):

        with open(title,"a") as f:
            for i in text1:
                f.write(i)
            f.write("\n")
            for j in text2:
                f.write(j)
            f.write("\n")

def main():

    getURL_Title()
    driver_item.quit()

main()

