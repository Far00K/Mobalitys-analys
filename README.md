# Mobalitys-analys
A python program that scrapes stats and data from decks in a tier list in the game LOR(league of runterra)


In this project we are scraping stats and deck codes from "https://lor.mobalytics.gg/stats/decks". Using Selenium and bs4 we are extracting deck codes, winrates, pick rates,
total matches played. Mobalytics loads more decks by scrolling down the web page. To solve this we're using Selenium to imitate this action with page down to retrive the data needed. 
                   
With the stats taken the next step is to change the url so it searches for a specfic deck. by using the deck code we can add it to the url to get details about the wanted deck. Doing this for every deck in the tier list we can get the stats and what type of deck it is and card it uses.
