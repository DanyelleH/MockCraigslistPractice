from django.contrib import admin
from django.urls import path, include
from .views import AllCategories, AllPostsInCategory, CategoryById, PostById
urlpatterns = [
    path('', AllCategories.as_view(), name="all_categories"),
    path("<int:category_id>/", CategoryById.as_view(), name="cat_by_id"),
    path("<int:category_id>/posts", AllPostsInCategory.as_view(), name="posts_in_cat"),
    path("<int:category_id>/posts/<int:post_id>", PostById.as_view(), name="post_by_id")
]