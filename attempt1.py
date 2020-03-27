from selenium.webdriver import Chrome
import time
import json

webdriver = "/Users/levon/Documents/coding/temporary_paath/chromedriver"

driver = Chrome(webdriver)

URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

driver.get(URL)

test = driver.find_element_by_xpath("/html/body").text

URL2 = "https://www.csvjson.com/csv2json"

driver.get(URL2)

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/textarea").clear()

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/textarea").send_keys(test)

time.sleep(2)

# pop up box exit click
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/a").click()

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/button[1]").click()

time.sleep(10)

test3 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/textarea").get_attribute('value')

with open("covid19_data.json", "w") as outfile:
    outfile.write(test3)