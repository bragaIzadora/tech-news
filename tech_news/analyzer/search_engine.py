from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    title = title.lower()

    results = db.news.find({"title": {"$regex": title, "$options": "i"}},
                           {"title": 1, "url": 1})

    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    formatted_date = date_obj.strftime("%d/%m/%Y")

    results = db.news.find({"timestamp": formatted_date},
                           {"title": 1, "url": 1})

    return [(result["title"], result["url"]) for result in results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
