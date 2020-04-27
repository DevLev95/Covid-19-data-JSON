import json
import itertools


states_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


all_states = {}

for state in states_list:
    state_obj = {}
    state_obj["name"] = state
    state_obj["cities"] = []
    all_states[state] = state_obj

print (all_states)

with open("/Users/levon/PycharmProjects/Covid19/update1_time_series/update1_daily_data/4-18-20.json", 'r') as myfile:
    data = myfile.read()

daily_object = json.loads(data)

for county in daily_object:
    state_name = county["Province_State"]
    county_name = county["Admin2"]
    if state_name in states_list:
        all_states[state_name]["cities"].append(county["Admin2"])

list = list(all_states.values())
print(list)

JSON = json.dumps(list)


with open("/Users/levon/PycharmProjects/Covid19/update1_time_series/update1_counties/dropdown_county_labels_WORKING.json", "w") as outfile:
    outfile.write(JSON)