from news.models import News

def get_news(**kwargs):
    news = News.objects.all()
    return news