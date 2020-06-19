from robot.libraries.BuiltIn import BuiltIn
import re
from importlib import import_module
from robot.libraries import DateTime
import os
from pythonfw.core import root
import winreg

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