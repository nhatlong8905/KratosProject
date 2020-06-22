'''
Created on Jun 22, 2020

@author: nhat.phan
'''
from collections import namedtuple
import json

from pythonfw.api.KratosAPIBase import KratosAPIBase
from pythonfw.apiobject.Network import Network
from pythonfw.apiobject.NetworkSettings import NetworkSettings
from pythonfw.apiobject.dataObject import dataObject
from pythonfw.core.assertion import Assert
from pythonfw.core.helpers import logger
from pythonfw.utilities.api_object_helper import get_endpoint_api, \
    load_data_for_apis

class NetworkSettingsAPI(KratosAPIBase):
    
    def __init__(self):
        KratosAPIBase.__init__(self)
        self._basePath = get_endpoint_api(self)
        self._networkObject = load_data_for_apis(self)
        self._response=""
         
    def get_network_configuration(self):
        self._response = self.client.get(self.basedPath, headers=self._make_header())
        logger.info("respond json: " + json.dumps(self._response.json()))
        return self._response    
     
    def check_status_network_configuration(self):
        if self._response:
            logger.info("status_code: " + str(self._response.status_code))
            Assert.should_be_equal_as_integers(200, self._response.status_code, "Actuality is" +str(self._response.status_code), "Expectation is "+ str(200))
    
    def verify_list_network_configuration_information(self, count = None, uri = None, hostname = None):
        if self._response:
            netwRespond = self._response.json()
            lstNetWork= self.getlstItem(netwRespond['items']);
            dataJson= dataObject(json.dumps(lstNetWork[0].data))
            logger.info("count: " + str(netwRespond['count']))
            logger.info("uri: " + lstNetWork[0].uri)
            logger.info("dataJson.hostName" + dataJson.hostName)
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
        self._response = self.client.put(self.basedPath +"/"+ number, headers=headers, data=requestData)
        logger.info("respond json updated: " + json.dumps(self._response.json()))
        return self._response
    
    def verify_network_configuration_information(self, uri = None, hostname = None):
        if self._response:
            dataNW = self._response.json()
            netWork= Network(dataNW['uri'],dataNW['data']);
            dataJson= dataObject(json.dumps(netWork.data))
            if uri:
                Assert.should_be_equal(netWork.uri,uri)
            if hostname:
                Assert.should_be_equal(dataJson.hostName,hostname)
    def getlstItem(self, jsonArray):
        lstItemNW=[]
        for item in jsonArray:
            itemNW = Network(item['uri'],item['data'])
            lstItemNW.append(itemNW)
        return lstItemNW