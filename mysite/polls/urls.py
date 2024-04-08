from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('some_url', views.some_url),
]
