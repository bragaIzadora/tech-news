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
    selector = Selector(text=html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").re_first(r"\d{2}/\d{2}/\d{4}")
    writer = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").get().split()[0]
    )

    raw_summary = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()

    summary = "".join(raw_summary).strip()

    category = selector.css(".category-style .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
