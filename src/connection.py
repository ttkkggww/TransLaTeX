import requests
import json
import os

class Connection:
    def __init__(self):
        api_json = json.load(open("api.json",'r'))
        self.api_key = api_json["deepl_api"]
        print(self.api_key)
        print(type(self.api_key))

    def translate(self,text:str,source_lang:str = "JA",target_lang:str = "EN"):
        params = {
                "auth_key" : self.api_key,
                "text" : text,
                "source_lang" : source_lang, 
                "target_lang": target_lang 
                }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        res = ""
        for txt in result['translations']:
            res += txt["text"]
        return res


    
