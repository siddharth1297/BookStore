# Generated by Django 2.0.5 on 2018-09-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20180904_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(default='Add subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default='Add description', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.CharField(default='Add tag', max_length=50),
        ),
    ]
