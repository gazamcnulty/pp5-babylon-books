from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=254)
    info = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    books_written = models.ForeignKey(
        'Book', on_delete=models.SET_NULL, related_name="books_written", null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="authors", null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added = models.DateField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ["-added"]

    def __str__(self):
        return self.title

