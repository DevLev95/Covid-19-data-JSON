import json


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
    state['Country/Region'] = "US"
    state['Lat'] = "N/A"
    state['Long'] = "N/A"
    state["1/22/2020"] = 0
    state["1/23/2020"] = 0
    state["1/24/2020"] = 0
    state["1/25/2020"] = 0
    state["1/26/2020"] = 0
    state["1/27/2020"] = 0
    state["1/28/2020"] = 0
    state["1/29/2020"] = 0
    state["1/30/2020"] = 0
    state["1/31/2020"] = 0
    state["2/1/2020"] = 0
    state["2/2/2020"] = 0
    state["2/3/2020"] = 0
    state["2/4/2020"] = 0
    state["2/5/2020"] = 0
    state["2/6/2020"] = 0
    state["2/7/2020"] = 0
    state["2/8/2020"] = 0
    state["2/9/2020"] = 0
    state["2/10/2020"] = 0
    state["2/11/2020"] = 0
    state["2/12/2020"] = 0
    state["2/13/2020"] = 0
    state["2/14/2020"] = 0
    state["2/15/2020"] = 0
    state["2/16/2020"] = 0
    state["2/17/2020"] = 0
    state["2/18/2020"] = 0
    state["2/19/2020"] = 0
    state["2/20/2020"] = 0
    state["2/21/2020"] = 0
    state["2/22/2020"] = 0
    state["2/23/2020"] = 0
    state["2/24/2020"] = 0
    state["2/25/2020"] = 0
    state["2/26/2020"] = 0
    state["2/27/2020"] = 0
    state["2/28/2020"] = 0
    state["2/29/2020"] = 0
    state["3/1/2020"] = 0
    state["3/2/2020"] = 0
    state["3/3/2020"] = 0
    state["3/4/2020"] = 0
    state["3/5/2020"] = 0
    state["3/6/2020"] = 0
    state["3/7/2020"] = 0
    state["3/8/2020"] = 0
    state["3/9/2020"] = 0
    state["3/10/2020"] = 0
    state["3/11/2020"] = 0
    state["3/12/2020"] = 0
    state["3/13/2020"] = 0
    state["3/14/2020"] = 0
    state["3/15/2020"] = 0
    state["3/16/2020"] = 0
    state["3/17/2020"] = 0
    state["3/18/2020"] = 0
    state["3/19/2020"] = 0
    state["3/20/2020"] = 0
    state["3/21/2020"] = 0
    state["3/22/2020"] = 0
    state["3/23/2020"] = 0
    state["3/24/2020"] = 0
    state["3/25/2020"] = 0
    state["3/26/2020"] = 0
    state["3/27/2020"] = 0
    state["3/28/2020"] = 0
    state["3/29/2020"] = 0
    state["3/30/2020"] = 0
    all_states[str(str_state)] = state

with open("counties_pile.json", 'r') as myfile:
    data = myfile.read()

CTS_object = json.loads(data)

#print(CTS_object)

#print(all_states)

for county in CTS_object:
    state_name = county["Province_State"]
    if state_name in states_list:
        access_state = all_states[state_name]
        #print(access_state)
        #list_access_state = list(access_state.items())
        list_county = list(county.items())
        #print(list_access_state[5][0])
        #print(len(list_county))
        for y in range(12, len(list_county)):
            daily_cases = list_county[y][1] - list_county[y-1][1]
            #print(access_state[list_county[y][0]] )
            access_state[list_county[y][0]] = access_state[list_county[y][0]] + daily_cases
            #print(access_state[list_county[y][0]]) =

            #access_state[] = access_state[list_county[y][1]] + daily_cases
            #print(list_county[y][0])

#print(all_states)

export_list = []

for x in all_states:
    export_list.append(all_states[x])

obj_JSON = json.dumps(export_list)


with open("3-30-daily-states3.json", "w") as outfile:
    outfile.write(obj_JSON)




