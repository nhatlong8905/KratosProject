'''
Created on Jun 22, 2020

@author: nhat.phan
'''
class Network(object):
    def __init__(self, uri,data):
        self._uri= uri
        self._data= data
    @property
    def uri(self):
        return self._uri
    
    @uri.setter
    def uri(self,m_uri):
        self._uri = m_uri
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,m_data):
        self._data = m_data