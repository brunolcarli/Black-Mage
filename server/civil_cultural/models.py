from django.db import models
from django.contrib.auth import get_user_model


class Portal(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    founding_datetime = models.DateTimeField(
        auto_now_add=True
    )
    topics = models.ManyToManyField('civil_cultural.Topic')
    # TODO - add News
    rules = models.ManyToManyField('civil_cultural.Rule')
    # TODO - add Chat
    # TODO - add Users
    tags = models.ManyToManyField('civil_cultural.Tag')


class Topic(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    description = models.TextField()
    scope = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    creation_datetime = models.DateTimeField(
        auto_now_add=True
    )
    articles = models.ManyToManyField('civil_cultural.Article')
    topic_portal = models.ForeignKey(
        'civil_cultural.Portal',
        on_delete=models.CASCADE,
    )
    # TODO - add Tag


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    post_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    article_authors = models.CharField(
        max_length=500,
        blank=False,
        null=False,
    )
    abstract = models.CharField(
        max_length=1500,
        unique=True
    )
    body = models.TextField(
        blank=False,
        null=False,
        unique=True
    )
    references = models.TextField()
    pro_votes = models.IntegerField(default=0)
    cons_votes = models.IntegerField(default=0)
    publication_date = models.DateField(
        auto_now_add=True
    )
    questions = models.ManyToManyField('civil_cultural.Question')
    tags = models.ManyToManyField('civil_cultural.Tag')
    reports = models.ManyToManyField('civil_cultural.Report')
    similar_suggestions = models.ManyToManyField(
        'civil_cultural.SimilarSuggestion'
    )
    published_topic= models.ForeignKey(
        'civil_cultural.Topic',
        on_delete=models.CASCADE
    )


class SimilarSuggestion(models.Model):
    post_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    description = models.TextField()
    link = models.CharField(
        max_length=500,
        blank=False,
        null=False,
        unique=True
    )
    pro_votes = models.IntegerField(default=0)
    cons_votes = models.IntegerField(default=0)
    publish_datetime = models.DateTimeField(
        auto_now_add=True
    )


class Question(models.Model):
    post_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    text = models.TextField(
        null=False,
        blank=False
    )
    pro_votes = models.IntegerField(default=0)
    cons_votes = models.IntegerField(default=0)
    publish_datetime = models.DateTimeField(
        auto_now_add=True
    )
    published_article = models.ForeignKey(
        'civil_cultural.Article',
        on_delete=models.CASCADE
    )
    # answers = models.ManyToManyField('civil_cultural.Answer')


class Report(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    report_datetime = models.DateTimeField(
        auto_now_add=True
    )
    # TODO - add Problem
    # TODO - add ProblemType (maybe a choices)


class Rule(models.Model):
    description = models.CharField(
        max_length=400,
        blank=False,
        null=False,
        unique=True
    )
    creation_date = models.DateField(
        auto_now_add=True
    )


class Tag(models.Model):
    reference = models.CharField(
        max_length=80,
        blank=False,
        null=False,
        unique=True
    )
