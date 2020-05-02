import json
import itertools
import csv
import re

states_list = ["Alabama","Alaska","American Samoa","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","District of Colombia","Florida","Georgia","Guam","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Northern Mariana Islands","Ohio","Oklahoma","Oregon","Pennsylvania","Puerto Rico",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Virgin Islands",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

file = open("state_routes.txt", "w")

for state in states_list:
    file.write("<Route path=\"/" + state + "\"render={(props) => <ChartSelectorStates info=\"" + state + "\" chart_type={this.state.selected_chart_type} isAuthed={true} />}/>")
    file.write("\n")

file.close()



