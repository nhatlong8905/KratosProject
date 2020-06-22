'''
Created on Jun 17, 2020

@author: nhat.phan
'''
import json

from pythonfw.api.KratosAPIBase import KratosAPIBase
from pythonfw.apiobject.Network import Network
from pythonfw.apiobject.Server import Server
from pythonfw.apiobject.dataObject import dataObject
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
#         logger.info("respond: " + json.dumps(self._response.json()))
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
    
    def verify_network_configuration_information_more(self, uri = None, name = None, ip = None):
        if self._response:
            #jsonRe = self._response.json()
            serverRespond = Server(self._response.json())
            if uri:
                Assert.should_be_equal(serverRespond.uri,uri)
            if name:
                Assert.should_be_equal(serverRespond.name,name)
            if ip:
                Assert.should_be_equal(serverRespond.id,ip)
    def verify_network_configuration_information(self, count = None, uri = None, hostname = None):
#         if self._response:
            #netwRespond = self._response.json()
            '''test'''
            with open("Data/testNetWork.json") as f:
                netwRespond = json.load(f)
            
            lstNetWork= self.getlstItem(netwRespond['items']);
            dataJson= dataObject(json.dumps(lstNetWork[0].data))
            if count:
                Assert.should_be_equal_as_integers(netwRespond['count'],count)
            if uri:
                Assert.should_be_equal(lstNetWork[0].uri,uri)
            if hostname:
                Assert.should_be_equal(dataJson.hostName,hostname)
    
    def update_network_configuration_hostname(self,number, hostname):
        requestData = { "hostName": hostname}
        requestData = json.dumps(requestData)
        
        headers = self._make_header({'Content-Type': 'application/json' })
        logger.info("Request data: " + requestData)
        resp = self.client.put(self.basedPath +"/"+ number, headers=headers, data=requestData)
        return resp
    
    def getlstItem(self, jsonArray):
        lstItemNW=[]
        for item in jsonArray:
            itemNW = Network(item['uri'],item['data'])
            lstItemNW.append(itemNW)
        return lstItemNW
    
    
    