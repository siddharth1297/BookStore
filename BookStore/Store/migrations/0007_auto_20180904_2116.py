# Generated by Django 2.0.5 on 2018-09-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]