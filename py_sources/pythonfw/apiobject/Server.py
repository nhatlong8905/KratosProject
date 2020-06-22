'''
Created on Jun 22, 2020

@author: nhat.phan
'''
class Server(object):
    def __init__(self, data):
        #self.__dict__ = json.loads(data)
        self._uri= data['uri']
        self._name= data['data']['name']
        self._serverTime= data['data']['serverTime']
        self._id= data['data']['id']
    @property
    def uri(self):
        return self._uri
    
    @uri.setter
    def uri(self,m_uri):
        self._uri = m_uri
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,m_name):
        self._name = m_name
    
    @property
    def servertime(self):
        return self._servertime
    
    @servertime.setter
    def servertime(self,m_servertime):
        self._servertime = m_servertime
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,m_id):
        self._id = m_id