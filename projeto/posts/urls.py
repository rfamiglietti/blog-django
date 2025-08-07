# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para a página inicial
]