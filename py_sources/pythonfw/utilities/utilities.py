'''
Created on Mar 11, 2020

@author: tiep.tra
'''
import win32serviceutil
from pythonfw.core.assertion import Assert
from PIL import Image, ImageChops 
import time
import os
import _csv
from pythonfw.core.helpers import logger
from pythonfw.core import OS

class Utilities():
    
    def replace_substring_in_text_file(self, locationFile, substring, newValue):
        file = open(locationFile, "r")
        data = file.read()
        file.close()
        data = data.replace(substring, newValue)
        file = open(locationFile, "w")
        file.write(data)
        file.close()
    
    def get_windows_service(self, serviceName):
        return win32serviceutil.QueryServiceStatus(serviceName)[1]
    
    def start_service(self, serviceName):
        status = self.get_windows_service(serviceName)
        if status != 4 and status != 2:
            win32serviceutil.StartService(serviceName)
            status = self.get_windows_service(serviceName)
            while(status != 4):
                time.sleep(0.5)  # wait for started service
                status = self.get_windows_service(serviceName)
    
    def stop_service(self, serviceName):
        status = self.get_windows_service(serviceName)
        if status != 1 and status != 7:
            win32serviceutil.StopService(serviceName)
            status = self.get_windows_service(serviceName)
            while(status != 1):
                time.sleep(0.5)  # wait for stopped service
                status = self.get_windows_service(serviceName)
        
    def restart_service(self, serviceName):
        self.stop_service(serviceName)
        self.start_service(serviceName)

    def get_windows_user(self):
        return os.getlogin()
    
    def check_download_file_exist(self, fileName):
        currentWindowsUser = self.get_windows_user()
        downloadFolderPath = "C:\\Users\\" + currentWindowsUser + "\\Downloads\\"
        os.path.exists(downloadFolderPath + fileName)
            
    def remove_file(self, path):
        if os.path.exists(path):
            os.remove(path)
        
    def copy_file(self, source, destination):
        OS.copy_file(source, destination)
        
    def reverse_list(self, inputList):
        return list(reversed(inputList))
