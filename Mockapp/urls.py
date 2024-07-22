from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import categories, posts, users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Root path
    path('', users.welcome_index, name='welcome_index'),

    # User paths
    path('sign_up/', users.register, name='sign_up'),
    path('login/', users.login_view, name='login'),
    path('logout/', users.logout_view, name='logout'),

    # Post paths
    path('posts/', posts.post_index, name='post_index'),
    path('posts/new', posts.new_post, name='new_post'),
    path('posts/<int:pk>/', posts.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', posts.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', posts.post_delete, name='post_delete'),
    path('users/<int:user_id>/my_posts/', posts.user_posts, name='my_posts'),

    # Category paths
    path('categories/', categories.category_list, name='category_list'),
    path('categories/new/', categories.category_create, name='category_create'),
    path('categories/<int:pk>/', categories.category_posts, name='category_detail'),
    path('categories/<int:pk>/edit/', categories.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', categories.category_delete, name='category_delete'),
    path('categories/<int:category_id>/posts/', categories.category_posts, name='category_posts'),

    # Comment paths
    path('post/<int:post_id>/comment/add', posts.add_comment, name='add_comment'),
    path('post/<int:post_id>/comment/<int:comment_id>/delete/', posts.delete_comment, name='delete_comment'),

    # Offline functionalities
    path('manifest.json', TemplateView.as_view(template_name="manifest.json", content_type="application/json")),
    path('serviceworker.js', TemplateView.as_view(template_name="serviceworker.js", content_type="application/javascript")),
]