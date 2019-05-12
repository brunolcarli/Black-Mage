from django.db import models
from django.contrib.auth import get_user_model

class News(models.Model):
    '''
    Modelo de dados para publicação de uma notícia.
    '''
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    votes = models.IntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT
        )


