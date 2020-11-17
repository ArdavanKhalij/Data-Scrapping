######### Libraries #########

import requests
from bs4 import BeautifulSoup

######### Libraries #########
########## Welcome ##########

print("Hello Dr. Asim Shrestha, Welcome!")

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

MyURL = 'https://www.tigerdroppings.com/rant/lsu-sports/'
r = requests.get(MyURL)
soup = BeautifulSoup(r.text, 'html.parser')
Topics = soup.find_all('h2')
RepliesAndDates = soup.find_all('td', attrs={'class':'TopicCenter'})
NameOfStarter = soup.find_all('div', attrs={'class':'Text nodt'})
FinalTopics = GetTheTopic(Topics)
FinalNameOfStarter = GetTheStarterName(NameOfStarter)
FinalReplies = GetTheNumberReplies(RepliesAndDates)
FinalDates = GetTheNumberDates(RepliesAndDates)

######### Main Page #########
