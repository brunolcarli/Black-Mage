# models
from news.models import News


def get_news(**kwargs):

    # filtros
    author = kwargs.get('author')
    title_contains = kwargs.get('title_contains')
    body_contains = kwargs.get('body_contains')

    # se fornecer filtro por autor, traz somente as noticias do autor
    if author:
        news = News.objects.filter(author=author)


    else:
        news = News.objects.all()

        if title_contains and body_contains:
            filtered_news = [n for n in news if title_contains.lower() in n.title.lower()]
            filtered_news += [n for n in news if body_contains.lower() in n.body.lower()]
            return filtered_news

        else:
            if title_contains and not body_contains:
                news = [n for n in news if title_contains.lower() in n.title.lower()]
                    
            if body_contains and not title_contains:
                news = [n for n in news if body_contains.lower() in n.body.lower()]

    return news