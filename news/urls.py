from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-news/', views.all_news, name='all_news'),
    path('news/<int:pk>/', views.read_news, name='read_news'),
    path('category/<slug:slug>/', views.news_by_category, name='news_by_category'),
    path('search/', views.search, name='search'),
    path('search-results/', views.search_results, name='search_results'),
]