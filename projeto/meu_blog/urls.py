# meu_blog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # Inclui as URLs do app 'posts' na rota raiz
]