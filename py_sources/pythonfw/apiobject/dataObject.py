'''
Created on Jun 22, 2020

@author: nhat.phan
'''
import json


class dataObject(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)