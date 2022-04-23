from django.urls import path
from . import views

app_name = 'guess'
urlpatterns = [
    path('', views.index),
    path('<int:guessvalue>', views.guess),
]