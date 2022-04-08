import configparser
from pathlib import Path


class ConfigFileParser():
    configFile = 'env.ini'
    configFileDirectory = 'config'
    config = configparser.ConfigParser()

    def __init__(self, cfg=configFile):

        self.configFile = cfg
        self. BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.configFileDirectory).joinpath(self.configFile)
        self.config.read(self.CONFIG_FILE)

    def getBaseUrl(self):
        return (self.config['nexport']['baseUrl'])

    def getLogin(self):
        return (self.config['nexport']['login'])

    def getPassword(self):
        return (self.config['nexport']['password'])

if __name__ == '__main__':
    config = ConfigFileParser()
    print(config.getBaseUrl())


