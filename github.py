from selenium.webdriver import Chrome
import time

webdriver = "/Users/levon/Documents/coding/temporary_paath/chromedriver"

driver = Chrome(webdriver)

URL = "https://github.com/LevonAr/LevonAr.github.io/blob/master/covid/data.json"

driver.get(URL)

driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div[3]/div[1]/div[2]/div[2]/form[1]/button/svg/path").click()

