from django.db import models


class News(models.Model):
    '''
    Modelo de dados para publicação de uma notícia.
    '''
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    votes = models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)
