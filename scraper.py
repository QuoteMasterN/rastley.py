from bs4 import BeautifulSoup
import requests

# read knownLinks.txt into a list
file = open("knownLinks.txt", "r")
knownLinks = file.readlines()

def searchForRick(url):
    # check if url is rick roll
    if url in knownLinks: return True

    # open url
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    # get links from page
    links = soup.find_all('a')

    # iterate through all links to check for rick rolls
    for link in links:
        if link in knownLinks:
            return True
    
    return False


