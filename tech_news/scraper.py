import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)

    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)

    news_cards = selector.css('.cs-overlay a::attr(href)').getall()

    return news_cards


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_link = selector.css('.next::attr(href)').get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
