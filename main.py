import json
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from base import kakao
from proxy_randomizer import RegisteredProviders
from fake_headers import Headers
from user_agent import generate_user_agent

def get_new_items():
    driver.refresh()
    try:
        driver.find_element(By.CSS_SELECTOR, "#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > a > div > span").click()
    except:
        pass
    new_items = []
    for item in driver.find_element(By.CSS_SELECTOR, "#block-freitag-content > article > section:nth-child(2) > div > div > div > div > div > div > div > div > div > div.flex.flex-wrap > div:nth-child(n) > div > img"):
        image_src = item.get_attribute("src")
        if image_src not in curr_items:
            new_items.append(image_src)
            curr_items.append(image_src)
    return new_items

def call():
    new_items = get_new_items()
    print("called")

    if new_items:
        for i in range(0, len(new_items)//3+1):
            if new_items[i*3:(i+1)*3]:
                self.kakao.send_to_kakao(new_items[i*3:(i+1)*3])
    else:
        print("Nothing New")

def proxy_create():
    rp = RegisteredProviders()
    rp.parse_providers()
    proxy = rp.get_random_proxy()
    return proxy

def main():    
    options = webdriver.ChromeOptions()
    # userAgent = generate_user_agent(os='win', device_type='desktop')
    
    rproxy = proxy_create()
    header = Headers(
                    browser="chrome",  # Generate only Chrome UA
                    os="win",  # Generate ony Windows platform
                    headers=True  # generate misc headers
                )
    headers = header.generate()
    proxies = 'http://%s' % self.proxy
    options.add_argument('--proxy-server=%s' % rproxy)
    options.add_argument("--incognito")
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome("./chromedriver.exe", options=options, headers=headers, proxies=proxies)
    driver.implicitly_wait(10)
    url = "https://www.freitag.ch/en/f304-moss"
    
    # self.randomproxy.crawling(url)
    
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div > div > div:nth-child(3) > a").click()

    curr_items = []
    call()

if __name__ == "__main__":
    main()