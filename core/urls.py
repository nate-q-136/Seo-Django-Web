from django.urls import path
from .views.main_page import index

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),  
    path('about/', index, name='about'),
    path('contact/', index, name='contact'),
    path('post/<int:pk>/<str:slug>', index, name='post_detail'),
    path('category/<int:pk>/', index, name='category-detail'),
    path('tag/<int:pk>/', index, name='tag-detail'),
    path('search/', index, name='search'),
]