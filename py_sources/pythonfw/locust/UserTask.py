'''
Created on Jun 15, 2020

@author: nhat.phan
'''
import logging
from locust import HttpUser
from locust.user.task import task
class UserTask(HttpUser):
    
    host= "http://lgus3034-2k12:5555"
    #tasks = [UserBehavior]
    def on_start(self):
        self.token = self.login()
        self.headers = {'Authorization': 'Token ' + self.token,'Content-Type' : 'application/json'}
         
    def login(self):
        response = self.client.post("/rest/Token", data={'user':'admin', 'password':'kratos'})
        logging.info("response= "+ response.text)
        return response.text
 
    @task(1)
    def get_list_server(self):
        a = self.client.get("/rest/Server/Server",headers=self.headers)
        logging.info("getListServer= "+ a.text)
    min_wait = 1000
    max_wait = 2000
        