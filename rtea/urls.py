from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('rtea/', views.tea, name='tea'),
]