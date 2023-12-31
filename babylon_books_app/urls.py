from django.contrib import admin
from django.urls import path, include
from . import views
from .views import handler404

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/', views.books, name='books'),
    path('book_detail<int:book_id>/', views.book_detail, name='book_detail'),
    path('search_results/', views.search_results, name='search_results'),
    path('about/', views.about, name='about'),
    path('bag/', views.bag, name='bag'),
    path('add_to_bag<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust_bag<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove, name='remove'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_product<int:product_id>/',
         views.edit_product, name='edit_product'),
    path('delete_product<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('blog/', views.blog, name='blog'),
    path('post_like<int:post_id>/', views.post_like, name='post_like'),
    path('blog_detail<int:post_id>', views.blog_detail, name='blog_detail'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('delete_review/<review_id>',
         views.delete_review, name='delete_review'),
    path('add_blogpost/', views.add_blogpost, name='add_blogpost'),

]

handler404 = 'babylon_books_app.views.handler404'
