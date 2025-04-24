'''
App Name: Headline Scraper & Sorter
Input: URL of a news site (CNN and BBC)
Output: Sorted list of headlines based on a selected strategy

Spencer Jackson
Intro to Software Development
'''

# Creational - Factory Method

from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class SiteParser(ABC):
    @abstractmethod
    def get_headlines(self, url):
        pass

class CNNParser(SiteParser):
    def get_headlines(self, url: str) -> list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_tags = soup.select('span.container__headline-text')
        print(f"Found {len(headline_tags)} headlines.")
        return [tag.get_text(strip=True) for tag in headline_tags]



class BBCParser(SiteParser):
    def get_headlines(self, url: str) -> list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_tags = soup.select('h2[data-testid="card-headline"]')
        print(f"Found {len(headline_tags)} headlines.")
        return [tag.get_text(strip=True) for tag in headline_tags]

from urllib.parse import urlparse

class ParserFactory:
    @staticmethod
    def get_parser(url: str) -> SiteParser:
        domain = urlparse(url).netloc
        if 'cnn.com' in domain:
            return CNNParser()
        elif 'bbc.com' in domain:
            return BBCParser()
        else:
            raise ValueError(f"No parser available for domain: {domain}")
