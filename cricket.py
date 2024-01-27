from bs4 import BeautifulSoup
import requests

url = 'https://www.cricbuzz.com/live-cricket-scores/78628/eng-vs-ind-1st-test-england-tour-of-india-2024'

response = requests.get(url)  # Fix the typo here, change 'request' to 'requests'
soup = BeautifulSoup(response.text, 'lxml')
score_card = soup.find('div', class_='cb-col-100 cb-col cb-col-scores').span.text
print("current Score in the format{}".format(score_card))
