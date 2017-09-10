# _*_ coding: utf-8 _*_
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

print('----------------SYSTEM LOADIUNG, please wait........')
SUMRESOURCES = 0 #全局变量
driver_item = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver_detail = webdriver.Chrome(executable_path='/Users/sallyfan/downloads/chromedriver')
url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
#等待页面家在方法
wait1 = ui.WebDriverWait(driver_item,15)
wait = ui.WebDriverWait(driver_detail, 15)

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
    number = int(input("ToP?:"))
    print('--------------------------')
    ask_long = int(input('dont need long comments, enter0, i like long commons enter 1:'))
    print('-===-----------------------------')
    global save_name
    save_name = input('save_name (xx.txt)')
    print('-----------------crawling')
    driver_detail.get(url)
    ##############################
    wait.until(
        lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]" % kind))
    driver_detail.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]" % kind).click()
    wait.until(
        lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]" % sort))
    driver_detail.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]" % sort).click()
    num = number + 1
    time.sleep(2)

    num_time = int(num/20)+1
    wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='content']/div/div[1]/div/div[4]/a") )

    for times in range(1, num_time):
        time.sleep(1)
        driver_detail.find_elements_by_xpath("//div[@class='list-wp']/a[@class='more']").click()
        time.sleep(1)
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]"%num))
    for i in range(1, num):
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]" % num))
        list_title = driver_detail.find_element_by_xpath("//*[@class='list']/a[%d]" % i)
        print('----------------------------------------------' + 'NO ' + str(SUMRESOURCES + 1) + '----------------------------------------------')
        print('电影名: ' + list_title.text)
        print('链接: ' + list_title.get_attribute('href'))  #unicode 转utf-8

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

def getDetails(urll, ask_long):
    driver_item.get(urll)
    # wait.until(lambda driver_item: driver_item.find_element_by_xpath("//*[@id='link-report']/span"))
    #time.sleep(3)
    drama = driver_item.find_element_by_xpath("//*[@id='link-report']/span").text


    print("剧情简介：")
    print(repr(drama))
    # drama_wr = drama.text.encode('utf-8')
    # Write_txt(drama_wr, '',save_name)
    print("------------------hot comments top------------")
    for i in range(1,5):
        try:
            comments_hot = driver_item.find_element_by_xpath("//*[@id='hot-comments']/div[%d]/div/p"%i).text
            print("最新热评：" + comments_hot)
            # comments_hot_wr = comments_hot.text.encode('utf-8')
            # Write_txt("------------------hot comments top%d-----------------------------------------------"%i,'',save_name)
            # Write_txt(comments_hot_wr,'',save_name)
        except:
            print( 'can not caught the comments!')
            # 加载长评
        if ask_long == 1:
            try:
                # driver_item.find_element_by_xpath("//div[@class = 'indicator j unfold']/a").click()
                driver_item.find_element_by_xpath("//div[@class='review-list']/div[1]/div/header/h3/div/a").click()
                print('click done')
                # wait1.until(lambda driver: driver.find_element_by_xpath("//div[@class='review-bd']/div[2]/div/div"))
                # time.sleep(1)
                # 解决加载长评会提示剧透问题导致无法加载
                comments_get = driver_item.find_element_by_xpath("//*[@id='link-report']/div[1]").text
                if comments_get == '提示: 这篇影评可能有剧透':
                    comments_deep = driver_item.find_element_by_xpath("//div[@class='review-bd']/div[2]/div[2]").text
                else:
                    comments_deep = comments_get
                print("--------------------------------------------long-comments---------------------------------------------")
                print("深度长评：" + comments_deep)
                # # comments_deep_wr = comments_deep.text.encode('utf-8')
                # Write_txt(
                #     "--------------------------------------------long-comments---------------------------------------------\n",
                #     '', save_name)
                # Write_txt(comments_deep_wr, '', save_name)
            except:
                print('can not caught the deep_comments!')
##############################################################################
#将print输出的写入txt中查看，也可以在cmd中查看，换行符是为了美观
##############################################################################
def Write_txt(text1='',text2='',title='douban.txt'):

        with open(title,"a") as f:
            for i in text1:
                f.write(str(i))
            f.write("\n")
            for j in text2:
                f.write(j)
            f.write("\n")

def main():

    getURL_Title()
    driver_detail.quit()

main()

