from collections import namedtuple
import json
from os import path

from pythonfw import rootfolder
from pythonfw.core.helpers import logger


mPageLocators = {}
apiFolder = rootfolder + "/apidata"
    
def load_data_for_apis(self):
    APIFile = "%s/%s.json" % (apiFolder, type(self).__name__)
    if not path.exists(APIFile):
        logger.warn("%s file doesn't exist" % APIFile)
        return False
    
    try:
        lstData = None
        with open(APIFile) as f:
            #jData = json.load(f)
            lstData = json.loads(f.read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return lstData     
    except Exception as e:
        if hasattr(e, 'message'):
            logger.warn(e.message)
        else:
            logger.warn(e)

        return False
def get_endpoint_api(self):
    
    EndPointFile = "%s/EndPoint.json" % (apiFolder)
    
    if not path.exists(EndPointFile):
        logger.warn("%s file doesn't exist" % EndPointFile)
        return False
    
    try:
        lstData = None
        with open(EndPointFile) as f:
            lstData = json.load(f)
        return lstData[ type(self).__name__]     
    except Exception as e:
        if hasattr(e, 'message'):
            logger.warn(e.message)
        else:
            logger.warn(e)

        return False

def get_data_api(self):
    endPoint = get_endpoint_api(self)
    jsBody = load_data_for_apis(self)
    return (endPoint,jsBody)
