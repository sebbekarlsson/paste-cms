from pymongo import MongoClient
from foliumer.config import config


client = MongoClient('localhost', 27017)
db = client[config['database']]
