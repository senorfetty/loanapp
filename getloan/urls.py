from django.urls import path
from . import views

urlpatterns = [
    path('getloan', views.home, name='home')
]