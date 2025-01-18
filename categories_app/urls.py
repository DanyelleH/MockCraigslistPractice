from django.contrib import admin
from django.urls import path, include
from .views import AllCategories
urlpatterns = [
    path('', AllCategories.as_view(), name="all_categories")
]