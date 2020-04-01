import json
with open('province_concat.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

new_obj = []

for country in obj:
    if not (country["Province/State"]):
        new_obj.append(country)

new_obj_JSON = json.dumps(new_obj)

with open("clean_data.json", "w") as outfile:
    outfile.write(new_obj_JSON)

