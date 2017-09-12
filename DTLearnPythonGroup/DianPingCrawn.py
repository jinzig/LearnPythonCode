# _*_ coding: utf-8 _*_
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
import select
import PIL
import asyncio

# shopID = int(input("input shopid please:  "))
# commpg = int(input("page number of shop:  "))

def comments_wods(shopID, commpg):
    uaList = (
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A334 Safari/7534.48.3'
        'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3',
        # 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        # 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1',
        'Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
        'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4',
        'Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00J Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G360T1 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:38.0) Gecko/38.0 Firefox/38.0',
        'Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0',
        'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G550T1 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        # 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.3.0',
        # 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]',
        # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) electron/1.0.0 Chrome/53.0.2785.113 Electron/1.4.3 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        # 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30'

    )

    dcap = dict(DesiredCapabilities.PHANTOMJS)


    # dcap["phantomjs.page.settings.userAgent"] = (uaList[random.randrange(0,len(uaList)+1)])

    pgno = 2
    all_comments = []
    while pgno <= commpg:
        dcap["phantomjs.page.settings.userAgent"] = (random.choice(uaList))
        # driver = webdriver.Chrome(executable_path='/Users/sallyfan/downloads/chromedriver')
        driver = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities= dcap)
        # driver = webdriver.Safari()
        url = "http://www.dianping.com/shop/%d/review_more?pageno=%d" % (shopID, pgno)
        driver.get(url)
        pgno +=1
        print(driver.desired_capabilities)

        comments_content = driver.find_elements_by_class_name("J_brief-cont")
        with open('dianping.txt', 'r+') as f:
            for i in comments_content:
                all_comments.append(i.text)
        pg_comment= "".join(all_comments)
        time.sleep(random.choice([1,2.1,1.7,0.5,1.5]))
        # f.write(pg_comment)

                # print (i.text)


        print(pg_comment)
        print(pgno)

    return pg_comment

            # f.write()



import jieba
wordlist = jieba.cut(comments_wods(6603735,30), cut_all = True)
word_space_split = " ".join(wordlist)

# print(comments_wods(16795494, 10))

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("/Users/sallyfan/downloads/mi.jpg"))
my_wordcloud = WordCloud(background_color = "white", max_words = 50000, mask = coloring, max_font_size = 30, random_state = 42, scale = 2, font_path = "/Users/sallyfan/downloads/msyh.ttf").generate(word_space_split)
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


    # print (comments_content)

