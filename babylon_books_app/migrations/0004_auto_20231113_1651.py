# Generated by Django 3.2.22 on 2023-11-13 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babylon_books_app', '0003_author_books_written'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books_written',
        ),
        migrations.AddField(
            model_name='author',
            name='books_written',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books_written', to='babylon_books_app.book'),
        ),
    ]
