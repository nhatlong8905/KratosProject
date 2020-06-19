import json

from pythonfw.config import constants
from pythonfw.core.utilities import utils


class UserConfig(object):

    @staticmethod
    def get_user_config(configKey=None, configFile=None):
        
        if configKey is None or configFile is None:
            configKey, configFile = utils.get_config_info("${CONFIGKEY}","${CONFIGFILE}")

        config = None
        try:
            with open(configFile) as f:
                data = json.load(f)
                item = data[configKey]
                config = UserConfig(
                                      item[constants.HOST_KEY],
                                      item[constants.USER_KEY],
                                      item[constants.PASSWORD_KEY],)
        except FileNotFoundError as fnfe:
            print (fnfe)
        return config

    def __init__(self, host, user, password):
        self._host = host
        self._user = user
        self._password = password
        self._mode = "user" if "".__eq__(host.strip()) else "admin"


    @property
    def mode(self):
        return self._mode
        
    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password