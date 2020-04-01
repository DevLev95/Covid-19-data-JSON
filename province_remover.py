import json
with open('province_concat.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

new_obj = []

for country in obj:
    if not (country["Province/State"] == ""):
        obj.remove(country)



obj_JSON = json.dumps(obj)

with open("bug_fix.json", "w") as outfile:
    outfile.write(obj_JSON)

