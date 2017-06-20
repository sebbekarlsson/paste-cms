from pymongo import MongoClient


config = {}
config['database'] = {}
config['database']['name'] = 'foliumer'

client = MongoClient('localhost', 27017)
db = client[config['database']['name']]
