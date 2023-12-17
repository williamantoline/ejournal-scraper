import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import config
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
filepath = config.storage_path


def get(masterUrl, n, slug, path):
    filename = filepath + str(slug) + ".titles.txt"

    with open(filename, "w") as file:
        for i in range(1, n+1):
            masterUrl = masterUrl + str(i)
            masterPageSoup = bsoup(urlopen(masterUrl))
            [el, class_] = path[0].split(".")
            masterMainDivs = masterPageSoup.find_all(el, class_=class_)
            
            for masterMainDiv in masterMainDivs:
                [el, class_] = path[1].split(".")
                journalUrl = masterMainDiv.find(el, class_=class_)['href']
                journalPageSoup = bsoup(urlopen(journalUrl))
                [el, class_] = path[2].split(".")
                journalMainDivs = journalPageSoup.find_all("div", class_=class_)

                for journalMainDiv in journalMainDivs:
                    [el, class_] = path[3].split(".")
                    articleTitle = journalMainDiv.find(el, class_=class_).find("a").text
                    file.write(formatTitle(articleTitle) + "\n")


def bsoup(page):
    return BeautifulSoup(page.read().decode("utf-8"), features="html.parser")

def formatTitle(title):
    return ' '.join(title.split())