import configparser
from pathlib import Path


configFile = 'env.ini'
configFileDirectory = 'config'
config = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(configFileDirectory).joinpath(configFile)

config.read(CONFIG_FILE)

def getBaseUrl():
    return (config['nexport']['baseUrl'])

def getLogin():
    return (config['nexport']['login'])

def getPassword():
    return (config['nexport']['password'])


print(getBaseUrl())
print(getLogin())
print(getPassword())