'''
Created on Jun 17, 2020

@author: nhat.phan
'''
from pythonfw import api
from pythonfw.config.user_config import UserConfig
from pythonfw.core.api import http

class KratosAPIBase:
    
    def __init__(self):
#         self._userConfig = UserConfig.get_user_config(configKey="user", configFile="Data/user_conf.json")
        self._userConfig = UserConfig.get_user_config()
        if self._userConfig:
            api.USERNAME = self._userConfig.user
            api.PASSWORD = self._userConfig.password
            api.HOST = self._userConfig.host
    @property
    def _access_token(self):
        if api.ACCESS_TOKEN:
            return api.ACCESS_TOKEN
        userload = 'user=%s&password=%s' % (api.USERNAME, api.PASSWORD)
        res= self.client.post("/rest/Token", data=userload)
        api.ACCESS_TOKEN = res.text
        return api.ACCESS_TOKEN
    
    @property
    def client(self):
        if api.CLIENT is None:
            api.CLIENT = http.target(api.HOST)
        return api.CLIENT
    
    def _make_header(self, headers: dict = {}):
        defaultHeader = { 'Authorization': '%s' % self._access_token}
        if headers:
            return {**defaultHeader, **headers}
        return defaultHeader