import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=254)
    info = models.TextField(blank=True)
    external_link = models.URLField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default='placeholder_image', blank=True)
    books_written = models.ForeignKey(
        'Book', on_delete=models.SET_NULL, related_name="books_written", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="authors", null=True, blank=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, related_name="genre", null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added = models.DateField(default=datetime.date.today)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='placeholder_image', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        ordering = ["-added"]

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=180, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.body
