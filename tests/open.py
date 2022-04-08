from configparser import ConfigParser
from config import*



config = ConfigParser()
print(config.sections())
print("-----------------")

config.read('pytest.ini')
print(config.sections())