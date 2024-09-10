from tech_news.database import db


# Requisito 7
def search_by_title(title):
    title = title.lower()

    results = db.news.find({"title": {"$regex": title, "$options": "i"}},
                           {"title": 1, "url": 1})

    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
