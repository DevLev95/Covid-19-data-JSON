import re

import json

import itertools

import time

with open('covid19_data.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

data_list = []

for country in obj:
    #print(country)
    new_object = {}
    #print(list(country.items())[0])
    list_country = list(country.items())
    #print(len(list_country))
    for i in range(0,5):
        key = list_country[i][0]
        value = list_country[i][1]
        #print(key,value)
        new_object[key] = value
    for j in range(6,len(list_country)):
        old_key = list_country[j][0]
        old_value = list_country[j][1]

        new_value = list_country[j][1] - list_country[j-1][1]

        new_object[old_key] = new_value

    data_list.append(new_object)
data_list_JSON = json.dumps(data_list)

with open("perDay2.json", "w") as outfile:
    outfile.write(data_list_JSON)
