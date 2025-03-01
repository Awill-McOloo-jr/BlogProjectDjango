from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),  # View all blogs
    path('create/', views.blog_create, name='blog_create'),  # Create a blog
    path('edit/<int:id>/', views.blog_edit, name='blog_edit'),  # Edit a blog
    path('delete/<int:id>/', views.blog_delete, name='blog_delete'),  # Delete a blog
]