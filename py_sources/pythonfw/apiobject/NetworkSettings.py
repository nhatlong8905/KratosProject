'''
Created on Jun 22, 2020

@author: nhat.phan
'''
from pythonfw.apiobject.Network import Network
from pydevd_attach_to_process.winappdbg.util import StaticClass
class NetworkSettings(object):
    def __init__(self, data):
        #self.__dict__ = json.loads(data)
        self._count= data['count']
        self.lstItem= data['items'] 
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self,m_count):
        self._count = m_count
    
    def getlstItem(self):
        lstItemNW=[]
        for item in self.lstItem:
            itemNW = Network(item['uri'],item['data'])
            lstItemNW.append(itemNW)
        return lstItemNW