# Generated by Django 2.2.5 on 2020-01-21 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_auto_20200122_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
