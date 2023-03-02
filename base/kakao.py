import requests
import json

class Kakao():
  def __init__(self):
    self.app_key = "cf10bb8dd2b330bddc0d7494b8be4d07" ## REST API 키 입력 

  # 저장 된 json 파일 읽어오기
    with open("kakao_token.json", "r") as fp:
        self.tokens = json.load(fp)

        self.refresh_token()



  # 카카오 토큰 갱신하기
  def refresh_token(self):
      url = "https://kauth.kakao.com/oauth/token"
      data = {
      "grant_type": "refresh_token",
      "client_id": self.app_key,
      "refresh_token": self.tokens['refresh_token']
      }

      response = requests.post(url, data=data)

      # 갱신 된 토큰 내용 확인
      result = response.json()

      # 갱신 된 내용으로 파일 업데이트
      if 'access_token' in result:
          self.tokens['access_token'] = result['access_token']

      if 'refresh_token' in result:
          self.tokens['refresh_token'] = result['refresh_token']
      else:
          pass

      with open("kakao_token.json", "w") as fp:
          json.dump(self.tokens, fp)



  def send_to_kakao(self, text):
      url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
      headers = {"Authorization": "Bearer " + self.tokens['access_token']}
      lists = [{"title": '가방', 
            "description": '새로운거',
            "image_url": str(elem),
            "image_width" : 50, "image_height" : 50,
            "link": {
                "web_url": "www.freitag.ch/en/f304-moss"
            }} for elem in lists]

      template = {
          "object_type" : "list",
          "header_title" : "mos",
          "header_link" : {
              "web_url" : "www.freitag.ch/en/f304-moss",
              "mobile_web_url" : "www.freitag.ch/en/f304-moss"
          },
          "contents" : lists,
          "buttons" : [
              {
                  "title" : "웹으로 이동",
                  "link" : {
                      "web_url" : "www.freitag.ch/en/f304-moss",
                      "mobile_web_url" : "www.freitag.ch/en/f304-moss"
                  }
              }
          ]
          
      }

      data = {
          "template_object" : json.dumps(template)
      }

      response = requests.post(url, data=data, headers=headers)
      if response.json().get('result_code') == 0:
          print('Success!')
      else:
          print('Failed. Error Message: ' + str(response.json()))