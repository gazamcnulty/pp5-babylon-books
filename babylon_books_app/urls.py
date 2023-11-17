from django.contrib import admin
from django.urls import path, include
from . import views

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
    path('remove_bag<item_id>/', views.remove_bag, name='remove_bag')
   
]
