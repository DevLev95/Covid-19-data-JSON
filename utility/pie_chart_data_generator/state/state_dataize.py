from selenium.webdriver import Chrome
import time
import json


# manually add USA stats to stat_data.json after running this script

# then manually remove commas and weird chars

#just try to  write a add a module that gets rid of this stuff sometime soon

states_list = ["Alabama","Alaska","American Samoa","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","District of Colombia","Florida","Georgia","Guam","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Northern Mariana Islands","Ohio","Oklahoma","Oregon","Pennsylvania","Puerto Rico",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Virgin Islands",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

webdriver = "/Users/levon/Documents/coding/temporary_paath/chromedriver"

driver = Chrome(webdriver)

URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States"

driver.get(URL)

time.sleep(1)

states_dict = {}

for i in range(1,57):
    state_series = []
    state_name = states_list[i-1]
    states_dict[state_name] = state_series


    for j in range(1,5):
                                                                                        #StateRow       #DataColumn
        element = driver.find_elements_by_xpath('//*[@id="covid19-container"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']')

        time.sleep(1)


        #grabs text out of element, equivalent to text()  this is a not a for loop that cycles through the states
        for value in element:
            state_series.append(value.text)
            print(value.text)
    #state_name = states_list[i-1]
    #states_dict[state_name] = state_series
                #print(cases, states_list[i-1], i)


obj_JSON = json.dumps(states_dict)

with open("state_data.json", "w") as outfile:
        outfile.write(obj_JSON)




driver.close()