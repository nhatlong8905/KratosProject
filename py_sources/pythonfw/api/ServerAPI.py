'''
Created on Jun 17, 2020

@author: nhat.phan
'''
import json
from pythonfw.api.KratosAPIBase import KratosAPIBase
from pythonfw.core.api.http_response import HTTPResponse
from pythonfw.core.assertion import Assert
from pythonfw.core.helpers import logger
from pythonfw.utilities.api_object_helper import load_data_for_apis, get_endpoint_api

class ServerAPI(KratosAPIBase):
    def __init__(self):
        KratosAPIBase.__init__(self)
        self.basedPath = get_endpoint_api(self)
        self._serverObject = load_data_for_apis(self)
        self._response=""

    def get_list_server(self):
        self._response = self.client.get(self.basedPath, headers=self._make_header())
        logger.info("respond: " + json.dumps(self._response.json()))
        return self._response
    
    def check_status_list_server(self):
        if self._response:
            logger.info("status_code: " + str(self._response.status_code))
            Assert.should_be_equal_as_integers(200, self._response.status_code, "Actuality is" +str(self._response.status_code), "Expectation is "+ str(200))
     
    def verify_server_information(self, name):
        if self._response:
            jsonRe = self._response.json()
            logger.info("name: " + jsonRe['data']['name'])
            Assert.should_be_equal(jsonRe['data']['name'], name, "Actuality is" + jsonRe['data']['name'], "Expectation is "+ name)
    
    def get_data_api(self):
        if self._serverObject:
            return self._serverObject.data.name
        