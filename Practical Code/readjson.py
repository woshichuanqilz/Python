import json
from pprint import pprint

with open('data2.json') as data_file:    
    data = json.load(data_file)


print data["colorxy"][0]["x"]
# print data["masks"]["id"]
# print data["om_points"]
