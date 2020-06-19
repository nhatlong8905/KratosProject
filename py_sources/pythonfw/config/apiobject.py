import json

from pythonfw.config import constants
from pythonfw.core.utilities import utils


class ApiObject(object):

    @staticmethod
    def get_json_file(apiKey=None, apiFile= None):
        if apiKey is None or apiFile is None:
            apiKey, apiFile = utils.get_config_info("${APIKEY}","${APIFILE}")

        config = None
        try:
            with open(apiFile) as f:
                data = json.load(f)
                item = data[apiKey]
                config = ApiObject(
                                      item[constants.ENDPOINT_KEY],
                                      item[constants.AUTHORIZATION_KEY],
                                      item[constants.CONTENT_KEY],
                                      item[constants.BODY_KEY],)
        except FileNotFoundError as fnfe:
            print (fnfe)
        return config
 
    def __init__(self, endpoint, authorization, content, body):
        self._endpoint = endpoint
        self._authorization = authorization
        self._content = content
        self._body = body
    
    @property
    def endpoint(self):
        return self._endpoint

    @property
    def authorization(self):
        return self._authorization

    @property
    def content(self):
        return self._content

    @property
    def body(self):
        return self._body