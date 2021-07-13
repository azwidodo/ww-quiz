from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



URL = "https://www.wizardingworld.com" + "/quiz/first-year-diagon-alley-quiz"
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(URL)

driver.execute_script("window.scrollBy(0,1000)")
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

try:
    start = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "UISubmit-component is-loaded QuizCover-start-button"))
    )

    print("FOUND")

except:
    print("Button not found")
    # driver.quit()
