import json
import itertools




# change both values





today = '4/4/2020'
yesterday = '4/3/2020'

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
    str_state = state
    state ={}
    state['Province/State'] = str(str_state)

    state[today] = 0
    all_states[str(str_state)] = state





# change file to todays data





with open("daily_data/4-4-20.json", 'r') as myfile:
    data = myfile.read()

daily_object = json.loads(data)

for county in daily_object:
    state_name = county["Province_State"]
    if state_name in states_list:
        access_state = all_states[state_name]

        #change this to current day
        access_state[today] = access_state[today] + county["Confirmed"]
        #print(access_state["Confirmed"])
        #print(county["Confirmed"])





# change file to yesterdays data




with open("./daily_data/4-3-20.json", 'r') as myfile:
    data1 = myfile.read()

yesterday_object = json.loads(data1)

for county in yesterday_object:
    state_name = county["Province_State"]
    if state_name in states_list:
        access_state = all_states[state_name]

        access_state[today] = access_state[today] - county["Confirmed"]

export_list = []

for x in all_states:
    export_list.append(all_states[x])





# change to yesterdays time_series





with open("./archived_time_series/states_up_to_4-3-20.json", 'r') as myfile:
    data2 = myfile.read()

update_object = json.loads(data2)

for state_old, state_new in zip(update_object, export_list):
    add_daily_value = state_new[today]
    state_old[today] = add_daily_value


obj_JSON = json.dumps(update_object)







#change file name to todays update






with open("./time_series_daily_update/states_up_to_4-4-20.json", "w") as outfile:
    outfile.write(obj_JSON)

with open("./archived_time_series/states_up_to_4-4-20.json", "w") as outfile:
    outfile.write(obj_JSON)