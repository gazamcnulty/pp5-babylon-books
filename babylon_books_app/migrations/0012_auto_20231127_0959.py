# Generated by Django 3.2.22 on 2023-11-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babylon_books_app', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=180, null=True),
        ),
    ]
