from bs4 import BeautifulSoup
import requests
import re

# read knownLinks.txt into a list
file = open("knownLinks.txt", "r")
knownLinks = file.readlines()

def searchForRick(url):
    links = []
    # check if url is rick roll
    if url in knownLinks: return True

    # open url
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    # get links from page
    for tag in soup.find_all(src=True):
        links.append(tag['src'])

    print(links)
    # iterate through all links to check for rick rolls
    for link in links:
        if link in knownLinks:
            return True
    
    return False


