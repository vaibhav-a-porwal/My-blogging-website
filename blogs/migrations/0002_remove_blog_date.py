# Generated by Django 3.1.5 on 2021-02-21 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
    ]
