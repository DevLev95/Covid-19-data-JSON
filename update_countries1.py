import json
with open('3-31-20.json', 'r') as myfile:
    data = myfile.read()

with open('perDay2.json', 'r') as nyfile:
    data2 = nyfile.read()

update_obj = json.loads(data)

archive_obj = json.loads(data2)

print(len(update_obj), len(archive_obj))

for (countryA, countryU) in zip(archive_obj,update_obj):
    list_countryA = list(countryA.items())
    list_countryU = list(countryU.items())
    #print(list_countryU[1])
    for i in range(69, len(list_countryU)):
        new_cases = list_countryU[i][1]-list_countryU[i-1][1]
        #list_countryA.append(list_countryU[i])
        #print(new_cases)



#list_country = list(country.items())
