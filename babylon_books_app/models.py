from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added = models.DateField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ["-added"]

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=254)
    info = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name