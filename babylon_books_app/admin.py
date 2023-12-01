from django.contrib import admin
from .models import Book, Author, Genre, Post, Review

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
    ordering = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Display fields for Genre model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Display fields for Book model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('title', 'added',)
    list_filter = ('added',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    """
    Display fields for Review model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('user', 'book', 'body', 'created_on')
    search_fields = ['user', 'book', 'body']
    list_filter = ('user', 'book', 'created_on')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Display fields for Post model in Django admin page
    Decorator ensures superuser access only , not for front end user
    """
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'created_on')
