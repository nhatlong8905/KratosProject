from collections import namedtuple
import json
from robot.libraries import DateTime
from robot.libraries.BuiltIn import BuiltIn

def get_config_info(variableKey,variableFile):
    robotBuiltin = BuiltIn()
    configKey = ""
    configFile = ""
    try:
        configKey = robotBuiltin.get_variable_value(variableKey)
        configFile = robotBuiltin.get_variable_value(variableFile)
    except Exception as e:
        print (e)
    return (configKey, configFile)
 
def get_current_date_time(timeZone='local', increment=0, resultFormat='timestamp', excludeMillis=False):
    return DateTime.get_current_date(timeZone, increment, resultFormat, excludeMillis)

def fatal_error(message=None):
    BuiltIn().fatal_error(message)

def getObjectFromJson(jsonFile):
    return json.loads(jsonFile, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

