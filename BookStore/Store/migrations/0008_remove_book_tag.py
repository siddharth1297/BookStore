# Generated by Django 2.0.5 on 2018-09-05 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_auto_20180904_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tag',
        ),
    ]
