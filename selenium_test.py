from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Launch Microsoft Edge (Chromium)
# PATH = "C:\Program Files (x86)\msedgedriver.exe"
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(executable_path=PATH, options=options)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.goodreads.com/")
print(driver.title)

search = driver.find_element_by_name("query")
search.send_keys("9780517884539")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()