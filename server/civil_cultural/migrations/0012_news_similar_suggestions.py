# Generated by Django 2.1.4 on 2019-07-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civil_cultural', '0011_auto_20190715_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='similar_suggestions',
            field=models.ManyToManyField(to='civil_cultural.SimilarSuggestion'),
        ),
    ]
