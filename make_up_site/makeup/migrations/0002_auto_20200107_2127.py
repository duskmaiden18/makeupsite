# Generated by Django 2.2.5 on 2020-01-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='care',
            name='pic',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='decorative',
            name='pic',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
