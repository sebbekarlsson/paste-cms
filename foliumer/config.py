import json


config = {}

with open('config.json') as conffile:
    config = json.loads(conffile.read())
conffile.close()
