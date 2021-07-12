import requests
from bs4 import BeautifulSoup


url = "https://www.wizardingworld.com" + "/quiz/first-year-diagon-alley-quiz"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

div = soup.find_all("div", {"class": "QuizQuestion-component is-loaded"})
print(div)
