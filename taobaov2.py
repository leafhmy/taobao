from selenium import webdriver
import time
import re
keyword = input("请输入商品名")
driver = webdriver.Chrome()
driver.get('http://www.taobao.com')

def search():
    driver.find_element_by_id('q').send_keys(keyword)
    driver.find_element_by_class_name('btn-search').click()
    time.sleep(10)
    taken = driver.find_element_by_xpath("//*[@id='mainsrp-pager']/div/div/div/div[1]").text
    taken = int(re.compile('\d+').search(taken).group(0))
    return taken

def next_page():
    taken = search()
    num = 0
    while num != taken - 1:
        driver.get('http://s.taobao.com/search?q={}&s={}'.format(keyword, 44*num))
        driver.implicitly_wait(10)
        num += 1
        drop_dowm()
        get_product()

def drop_dowm():
    for x in range(1, 11, 2):
        time.sleep(1)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' %j
        driver.execute_script(js)


def get_product():
    lis = driver.find_elements_by_xpath("//div[@class='items']/div[@class='item J_MouserOnverReq  ']")
    for li in lis:
        info = li.find_element_by_xpath(".//div[@class='pic']/a/img").get_attribute('src')
        print(info)
get_product()

if __name__ == '__main__':
    next_page()

