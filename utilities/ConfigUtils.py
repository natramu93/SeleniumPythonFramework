import configparser

class Config:
    config = configparser.ConfigParser()
    config.read('config/ProjectConfig.ini')
    print(config)
    def __init__(self,env):
        self.env = env

    def get_value(self,key):
        return self.config[self.env][key]
