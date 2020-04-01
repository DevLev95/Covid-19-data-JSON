import json
with open('perDay2.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

obj_list = list(obj[0].items())

new_china = {}
new_canada = {}
new_australia = {}

for i in range (0,len(obj_list)):
    new_china[obj_list[i][0]] = 0
    new_canada[obj_list[i][0]] = 0
    new_australia[obj_list[i][0]] = 0

#print(obj_list[0][0])

new_china['Province/State'] = ""
new_china['Country/Region'] = "All China"
new_china['Lat'] = "N/A"
new_china['Long'] = "N/A"

new_canada['Province/State'] = ""
new_canada['Country/Region'] = "All Canada"
new_canada['Lat'] = "N/A"
new_canada['Long'] = "N/A"

new_australia['Province/State'] = ""
new_australia['Country/Region'] = "All Australia"
new_australia['Lat'] = "N/A"
new_australia['Long'] = "N/A"


#China

for country in obj:
    if(country["Country/Region"] == "China"):
        list_country = list(country.items())
        for j in range(4,len(list_country)):
            new_china[list_country[j][0]] = new_china[list_country[j][0]] + list_country[j][1]

for country in obj:
    if(country["Country/Region"] == "Canada"):
        list_country = list(country.items())
        for j in range(4,len(list_country)):
            new_canada[list_country[j][0]] = new_canada[list_country[j][0]] + list_country[j][1]

for country in obj:
    if(country["Country/Region"] == "Australia"):
        list_country = list(country.items())
        for j in range(4,len(list_country)):
            new_australia[list_country[j][0]] = new_australia[list_country[j][0]] + list_country[j][1]


obj.append(new_china)
obj.append(new_canada)
obj.append(new_australia)

obj_JSON = json.dumps(obj)

with open("goddamnthis1.json", "w") as outfile:
    outfile.write(obj_JSON)


