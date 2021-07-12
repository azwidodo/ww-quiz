import requests
from bs4 import BeautifulSoup


def find_quiz_links():

    links = []

    for i in range(1, 15):
        url = f"https://www.wizardingworld.com/quiz/page/{i}"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        for a in soup.find_all('a', href=True):
            link = a['href']
            if link.startswith("/quiz/"):
                if link not in links:
                    links.append(link)

    return links


links = find_quiz_links()
# print(links)
print(len(set(links)))
