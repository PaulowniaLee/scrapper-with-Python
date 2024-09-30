import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #找出所有以“/”开头的链接
    for link in bsObj.findAll("a", href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有以http或www开头且不包括当前URL的链接
    for link in bsObj.findAll('a', 
                          href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", '').split('/')
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features='html.parser')
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        NextexternalLinks = getExternalLinks(internalLinks[random.randint(0,
                                    len(internalLinks)-1)])
        return NextexternalLinks[random.randint(0, len(NextexternalLinks)-1)]
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("https://en.wikipedia.org/wiki/Revue_Starlight")
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)

followExternalOnly('https://en.wikipedia.org/wiki/Love_Live!_Sunshine!!')




