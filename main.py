import json
import requests

from selenium import webdriver

from kakao import*

def get_new_items():
    driver.refresh()
    try:
        driver.find_element_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > a > div > span').click()
    except:
        pass
    new_items = []
    for item in driver.find_elements_by_css_selector('#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > div > div.flex.flex-wrap > div:nth-child(n) > div > img'):
        image_src = item.get_attribute('src')
        if image_src not in curr_items:
            new_items.append(image_src)
            curr_items.append(image_src)
    return new_items

def call():
    new_items = get_new_items()
    print('called')

    if new_items:
        for i in range(0, len(new_items)//3+1):
            if new_items[i*3:(i+1)*3]:
                self.kakao.send_to_kakao(new_items[i*3:(i+1)*3])
    else:
        print('Nothing New')

def __init__(self):
    self.kakao = Kakao()
    
if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')
    url = 'https://www.freitag.ch/en/f304-moss'
    driver.get(url)
    driver.find_element_by_css_selector('body > div:nth-child(6) > div > div > div:nth-child(3) > a').click()


    curr_items = []
    call()