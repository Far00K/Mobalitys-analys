from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import re

DeckCodeList = []
WinrateList = []
PickRateList = []
MatchesList = []

def write_csv(data):
    with open('result.csv', 'a') as f:
        fields = ['type', 'cards', 'amount']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(data)
    


url = "https://lor.mobalytics.gg/stats/decks"
Path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get(url)
time.sleep(2)

#scrolldown 

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

# scrape

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

deckCode = soup.findAll("a", {"class": "table-rowcomponent__TableRowAsLink-sc-5kpsac-1 eGnKgU _1E81P"})
winrate = soup.findAll("span", {"class": "win-ratecomponent__Wrapper-cyrb6r-1 ieygHL"})
pickrate = soup.findAll("span", {"class": "play-ratecomponent__Wrapper-sc-1fqm2b7-1 gjlQtw"})
matches = soup.findAll("span", {"class": "matches-countcomponent__MatchesCountWrapper-ypa9vh-1 fVLoPw"})

# sort

for post in winrate:
    WinrateList.append(post.text)

for post in deckCode:
    if post['href'][:12] == "/decks/code/":
        DeckCodeList.append('https://lor.mobalytics.gg' + post['href'])

for post in pickrate:
    PickRateList.append(post.text)

for post in matches:
    MatchesList.append(post.text)



def GetCardName(dc):
    driver.get(dc)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    types = soup.find("h1", {"class": "base-textcomponent__Text36x500-om21ho-1 app-page-header-layoutcomponent__AppPageHeaderLayoutTitle-uh7rmy-1 deck-details-header-base-infocomponent__AppPageHeaderLayoutTitleStyled-sc-7pmf6v-1 jivVIP"})
    typeList = types.text
    
    cards = soup.findAll("p", {"class": "base-textcomponent__Text14x500-om21ho-15 card-overviewcomponent__Title-sc-1uigtue-2 WTAyr"})
    cards_text = [i.text for i in cards]
    cardList = ', '.join(cards_text)
    
    amount = soup.findAll("p", {"class": "base-textcomponent__Text12x700-om21ho-19 cards-count-rectcomponent__CardCountValue-eilkv5-1 buZkqR"})
    amount_text = [i.text for i in amount]
    amountList = ', '.join(amount_text)

    data = {
            'type': typeList,
            'cards': cardList,
            'amount': amountList   
        }
    write_csv(data)



for i in DeckCodeList:
    GetCardName(i)


