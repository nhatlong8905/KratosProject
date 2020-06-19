'''
Created on Jun 17, 2020

@author: nhat.phan
'''

import json

from pythonfw.api.KratosAPIBase import KratosAPIBase
from pythonfw.config.apiobject import ApiObject 
from pythonfw.core.api.http_response import HTTPResponse
from pythonfw.core.helpers import logger
from pythonfw.core.assertion import Assert

class ServerAPI(KratosAPIBase):
    def __init__(self):
        KratosAPIBase.__init__(self)
        self._apiObject = ApiObject.get_json_file()
        self.basedPath = self._apiObject.endpoint 
        self._response=""

    def get_list_server(self):
        headers = self._make_header({'Content-Type': self._apiObject.content })
        self._response = self.client.get(self.basedPath, headers=headers)
        logger.info("respond: " + json.dumps(self._response.json()))
        return self._response
    
    def check_status_list_server(self):
        if self._response:
            httpRes = HTTPResponse(self._response)
            Assert.should_be_equal_as_integers(200, httpRes.status_code)
     
    def verify_server_information(self, name):
        if self._response:
            jsonRe = self._response.json()
            logger.info("name: " + jsonRe['data']['name'])
            Assert.should_be_equal(jsonRe['data']['name'], name)
            