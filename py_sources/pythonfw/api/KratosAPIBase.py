'''
Created on Jun 17, 2020

@author: nhat.phan
'''
from pythonfw import api
from pythonfw.config.user_config import UserConfig
from pythonfw.core.api import http
import logging
import requests
log = logging.getLogger("api")
class KratosAPIBase:
    
    def __init__(self):
#         self._userConfig = UserConfig.get_user_config()
#         if self._userConfig:
        api.USERNAME = "admin"
        api.PASSWORD = "kratos"
        api.HOST = "http://lgus3034-2k12:5555"
        api.TYPE_TOKEN = "Bearer"
        print(api.USERNAME)
        print(api.PASSWORD)
        print(api.HOST)
        print(api.TYPE_TOKEN)
        log.info("_userConfig: %s %s %s %s", api.USERNAME, api.PASSWORD,api.HOST, api.TYPE_TOKEN)
    @property
    def _access_token(self):
        if api.ACCESS_TOKEN:
            return api.ACCESS_TOKEN
        userload = 'user=%s&password=%s' % (api.USERNAME, api.PASSWORD)
        print(userload)
        res= self.client.post("/rest/Token", data=userload)
#         res = requests.post("https://10.244.125.77/rest/Token", data=userload, headers=headers, verify= False)
        api.ACCESS_TOKEN = res.json()
        print(res.text)
        log.info("api.ACCESS_TOKEN: %s", api.ACCESS_TOKEN)
#         return (api.TYPE_TOKEN, api.ACCESS_TOKEN)
        return api.ACCESS_TOKEN
    
    @property
    def client(self):
        if api.CLIENT is None:
            api.CLIENT = http.target(api.HOST)
        return api.CLIENT
    
    def _make_header(self, headers: dict = {}):
#         if api.TYPE_TOKEN=="":
#             defaultHeader = { 'Authorization': '%s' % api.ACCESS_TOKEN}
#         else:
#             defaultHeader = { 'Authorization': '%s %s' % self._access_token}
        defaultHeader = { 'Authorization':'Bearer %s' % self._access_token}
        if headers:
            return {**defaultHeader, **headers}
        log.info("api.ACCESS_TOKEN: %s", defaultHeader)
        return defaultHeader