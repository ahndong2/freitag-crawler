from fake_headers import Headers
from proxy_randomizer import RegisteredProviders
import requests

class RANDOM_PROXY:

    def __init__(self):
      self.proxy = self.proxy_create()
      # self.crawling()

    def proxy_create(self):
        rp = RegisteredProviders()
        rp.parse_providers()
        proxy = rp.get_random_proxy()
        return proxy
        
    def crawling(self, url):
       header = Headers(
                    browser="chrome",  # Generate only Chrome UA
                    os="win",  # Generate ony Windows platform
                    headers=True  # generate misc headers
                )
       self.headers = header.generate() # 랜덤 유저 에이전트를 생성해주는 함수.
       _url = url
       
       self.proxies = {} # request.get 인자에 넣어줄 딕셔너리 생성 
       self.proxies['http'] = 'http://%s' % self.proxy
       
       html = requests.Session().get(_url, headers=self.headers,proxies=self.proxies).content
       # get 인자에 프록시와 헤더를 넣어주면 끝.
       
    if __name__ == "__main__":
        print('dddddddddddddddddddddd')
        RANDOM_PROXY()