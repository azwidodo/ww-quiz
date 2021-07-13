from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



URL = "https://www.qzzr.com/widget/quiz/fi9xdWl6emVzLzQ4NTM4MD9zdGF0ZVtwX3VdPWh0dHBzJTNBJTJGJTJGd3d3LndpemFyZGluZ3dvcmxkLmNvbSUyRnF1aXolMkZmaXJzdC15ZWFyLWRpYWdvbi1hbGxleS1xdWl6JnN0YXRlW25dPW5vbmU"
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(URL)

driver.implicitly_wait(10)
start = driver.find_elements_by_tag_name("button")
print(start[0].class_name)
# print(start.get_attribute('innerHTML'))

# try:
#     start = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "translate-component is-loaded"))
#     )

#     print("FOUND")

# except:
#     print("Button not found")
#     # driver.quit()