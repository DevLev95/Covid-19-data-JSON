import json
import itertools
import csv
import re


with open("4-23-20.csv", "r") as counties:

    reader = csv.DictReader(counties)

    county_object = {}

    for row in reader:
        if row["Country_Region"] == "US":
            #define key
            comb_key = row["Combined_Key"]
            comb_key = re.sub(', US','',comb_key)

            # set up value which is an array
            county_fatality_series = []
            confirmed = row["Confirmed"]
            deaths = row["Deaths"]
            active = row["Active"]
            county_fatality_series.append(confirmed)
            county_fatality_series.append(deaths)
            county_fatality_series.append(active)

            county_object[comb_key] = county_fatality_series

    obj_JSON = json.dumps(county_object)

    with open("./county_data.json", "w") as outfile:
        outfile.write(obj_JSON)