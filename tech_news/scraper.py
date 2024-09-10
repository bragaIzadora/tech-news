import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def fetch_and_scrape_news(url, amount, collected_news):
    """Busca e processa notícias a partir de uma URL."""
    html_content = fetch(url)
    news_links = scrape_updates(html_content)

    news = []
    for news_url in news_links:
        if collected_news >= amount:
            break
        news_html = fetch(news_url)
        scraped_news = scrape_news(news_html)
        news.append(scraped_news)
        collected_news += 1

    next_page_url = scrape_next_page_link(html_content)

    return news, next_page_url, collected_news


def get_tech_news(amount):
    news = []
    url = "https://blog.betrybe.com/"
    collected_news = 0

    while collected_news < amount:
        scraped_news, next_page_url, collected_news = fetch_and_scrape_news(
            url, amount, collected_news)
        news.extend(scraped_news)

        if not next_page_url:
            break
        url = next_page_url

    create_news(news)

    return news
