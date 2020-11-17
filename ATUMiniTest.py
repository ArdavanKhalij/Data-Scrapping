######### Libraries #########

import requests
from bs4 import BeautifulSoup
import pandas as pd

######### Libraries #########
########## Welcome ##########

print("Hello Dr. Asim Shrestha, Welcome!")
print("It would take a while...")

########## Welcome ##########
####### Get the topic #######

def GetTheTopic(Topics):
    results = []
    for i in range(0, len(Topics)):
        results.append(Topics[i].find('a').text)
    return results

####### Get the topic #######
### Get the starter names ###

def GetTheStarterName(NameOfStarter):
    results = []
    for i in range(0, len(NameOfStarter)):
        temp = NameOfStarter[i].text
        temp2 = temp[3:]
        results.append(temp2[:-2])
    return results

### Get the starter names ###
# Get the number of replies #

def GetTheNumberReplies(Replies):
    results = []
    i = 0
    while i < len(Replies):
        results.append(int(Replies[i].text))
        i = i + 2
    return results

# Get the number of replies #
## Get the number of dates ##

def GetTheNumberDates(Dates):
    results = []
    i = 1
    while i < len(Dates):
        results.append(Dates[i].text[0:11])
        i = i + 2
    return results

## Get the number of dates ##
######### Main Page #########

records = []
MyURL = 'https://www.tigerdroppings.com/rant/lsu-sports/'
URLS = []
r = requests.get(MyURL)
soup = BeautifulSoup(r.text, 'html.parser')
Topics = soup.find_all('h2')
RepliesAndDates = soup.find_all('td', attrs={'class':'TopicCenter'})
NameOfStarter = soup.find_all('div', attrs={'class':'Text nodt'})
FinalTopics = GetTheTopic(Topics)
FinalNameOfStarter = GetTheStarterName(NameOfStarter)
FinalReplies = GetTheNumberReplies(RepliesAndDates)
FinalDates = GetTheNumberDates(RepliesAndDates)
for i in range(0, len(Topics)):
    URLS.append('https://www.tigerdroppings.com'+str(Topics[i].find('a')['href']))
for i in range(0, 3):
    r = requests.get(URLS[i])
    soup = BeautifulSoup(r.text, 'html.parser')
    comments = soup.find_all('div', attrs={'class': 'pText'})
    comment = comments[0].text
    records.append((FinalTopics[i], FinalNameOfStarter[i], FinalReplies[i], FinalDates[i], comment))
df = pd.DataFrame(records, columns=['Topic','Starter','Replies','Date','First_Comment'])
print("The output in a csv table form is ready.")

######### Main Page #########