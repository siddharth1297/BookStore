# Generated by Django 2.0.5 on 2018-09-07 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_remove_book_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(choices=[('', ''), ('Computer Architecture', 'Computer Architecture'), ('Operating System', 'Operating System'), ('Networking', 'Networking'), ('Distributed System', 'Distributed System'), ('Machine Learning', 'Machine Learning'), ('Deep Learning', 'Deep Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Algorithm', 'Algorithm'), ('Theoretical CS', 'Theoretical CS')], max_length=50),
        ),
    ]