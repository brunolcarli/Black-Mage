# Generated by Django 2.1.4 on 2019-07-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_mage', '0008_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='votes',
            new_name='cons_votes',
        ),
        migrations.AddField(
            model_name='news',
            name='pro_votes',
            field=models.IntegerField(default=0),
        ),
    ]
