# encoding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 用于实例化一个Driver的显式等待
from selenium.webdriver.common.by import By  # 内置定位器策略集
from selenium.webdriver.support import expected_conditions as EC  # 内置预期条件函数，具体API请参考此小节后API链接


#百度搜索
def GoogleWebBrowser1():
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.baidu.com')  # 获取百度页面
    inputbox = driver.find_element_by_id('kw')  # 获取输入框
    searchButton = driver.find_element_by_id('su')  # 获取搜索按钮
    a = input("hello....")
    inputbox.send_keys("Python")  # 输入框输入"Python"
    searchButton.click()  # 搜索
    time.sleep(60)
    return 0

# Bilibli
def GoogleWebBrowser2():
    driver = webdriver.Chrome()
    driver.get('https://www.bilibili.com/v/game/esports/?spm_id_from=333.334.primary_menu.35#/9222')
    try:
        WebDriverWait(driver, 20, 0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'vd-list')))  # 使用expected_conditions自带验证函数
        print(str(driver.find_elements_by_css_selector('.vd-list li')))
        for doctorName in driver.find_elements_by_css_selector('.vd-list li'):
            print(doctorName.find_element_by_css_selector('.r > a').text)
    finally:
        input("Press any KEy continue.....")
        driver.close()  # close the driver
    return 0

# 百度百科
def GoogleWebBrowser3():
    driver = webdriver.Chrome()
    driver.get('https://baike.baidu.com')
    inputbox = driver.find_element_by_id('query')  # 获取输入框
    searchButton = driver.find_element_by_id('search')  # 获取搜索按钮
    inputbox.send_keys("Geeks")  # 输入框输入"Python"
    searchButton.click()  # 搜索
    try:
        WebDriverWait(driver, 20, 0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'main-content')))  # 使用expected_conditions自带验证函数
        for doctorName in driver.find_elements_by_css_selector('.main-content h2'):
            print('data:'+doctorName.text)
    finally:
        input("Press any KEy continue.....")
        driver.close()  # close the driver
    return 0


# 美国国家医学图书馆
def GoogleWebBrowser4():
    driver = webdriver.Chrome()
    driver.get('https://pubchem.ncbi.nlm.nih.gov')
    inputbox = driver.find_element_by_xpath('//*[@id="search_1574427798159"]')  # 获取输入框
    searchButton = driver.find_element_by_css_selector("#main-content > div.search-bar-section.relative > div.main-width > div > div > div:nth-child(3) > form > div > div.main-search-submit > button")  # 获取搜索按钮
    inputbox.send_keys("Sarcosine")  # 输入框输入"Python"
    searchButton.click()  # 搜索
    try:
        WebDriverWait(driver, 20, 0.5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'f-medium p-sm-top p-sm-bottom f-1125')))  # 使用expected_conditions自带验证函数
        for doctorName in driver.find_elements_by_xpath('//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[1]/a'):
            print('data:'+doctorName.text)
    finally:
        input("Press any KEy continue.....")
        driver.close()  # close the driver
    return 0


if __name__ == '__main__':
    GoogleWebBrowser3()