# Generated by Django 3.2.22 on 2023-12-01 00:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('babylon_books_app', '0017_remove_comment_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
    ]
