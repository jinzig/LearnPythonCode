from selenium import webdriver

# url = 'http://www.dianping.com/shop/503472/review_more?pageno=2'
#
# browser = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
# browser.get(url)
# new_browsers = browser.find_elements_by_class_name('J_brief-cont')
# for i in new_browsers:
#     textnew_browers = i.get_attribute('textContent')
#     print(textnew_browers)

def pagenumber(shopID):

    browser = webdriver.PhantomJS(executable_path='/Users/sallyfan/downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    # url = 'http://www.dianping.com/shop/%d/review_more?pageno=1' % shopID

    url = 'http://www.dianping.com/shop/9964442/review_more?pageno=2'

    browser.get(url)
    pg_no = []
    try:

        pg_no = browser.find_element_by_xpath('//*[@id="top"]/div[4]/div[2]/div/div[2]/div[4]/div/a[10]').
    except:

        pass
    print (pg_no)




    # for i in pg_no0:
    #     print (i)



    # for i in pg_no:
    #     print(i)


    # while True:
    #     try:
    #         url = 'http://www.dianping.com/shop/%s/review_more?pageno=%d' % (shopID, pg_no)
    #         browser.get(url)
    #         pg_no += 1
    #         pg_tester = browser.find_elements_by_class_name('J_brief-cont')
    #         print(pg_no)
    #         # print(pg_no)
    #     except Exception:
    #         print('999')
    #         break

    # while True:
    #     try:
    #         url = 'http://www.dianping.com/shop/%s/review_more?pageno=%d' % (shopID, pg_no)
    #         browser.get(url)
    #         browser.find_element_by_class_name('heart-name')
    #         pg_no +=1
    #         print (pg_no)
    #     except Exception.message:
    #         print(pg_no)
    #         break



        #
        #     print("999")


print(pagenumber(9964442))