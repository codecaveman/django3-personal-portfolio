# Generated by Django 2.2 on 2020-03-26 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]