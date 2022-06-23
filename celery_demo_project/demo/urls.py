from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('celery_demo/', views.TestCeleryView.as_view()),
    path('celery_demo2/', views.TestCeleryView2.as_view()),
]
