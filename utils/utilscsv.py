import csv
from pathlib import Path

dataFile = 'data.csv'
configFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(configFileDirectory).joinpath(dataFile)

def get_data():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]
    return data


print(get_data())