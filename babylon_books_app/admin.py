from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Display fields for Author model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Display fields for Genre model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Display fields for Book model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('title', 'added',)
    list_filter = ('added',)
    search_fields = ('title',)



