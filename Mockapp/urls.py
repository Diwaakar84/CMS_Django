from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, PostViewSet, CategoryViewSet, CommentViewSet, LikeViewSet
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import categories, posts, users

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# # router.register(r'posts', PostViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'likes', LikeViewSet)

urlpatterns = [
    # Root path
    path('', users.welcome_index, name='welcome_index'),

    # User paths
    path('sign_up/', users.register, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', users.logout_view, name='logout'),
    # path('edit_profile/', users.edit_profile, name='edit_profile'),

    # Post paths
    path('posts/', posts.post_index, name='post_index'),
    path('posts/new', posts.new_post, name='new_post'),
    path('posts/<int:pk>/', posts.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', posts.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', posts.post_delete, name='post_delete'),
    # path('users/<int:user_id>/my_posts/', posts.user_posts, name='my_posts'),

    # Category paths
    path('categories/', categories.category_list, name='category_list'),
    path('categories/new/', categories.category_create, name='category_create'),
    path('categories/<int:pk>/', categories.category_posts, name='category_detail'),
    path('categories/<int:pk>/edit/', categories.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', categories.category_delete, name='category_delete'),
    path('categories/<int:category_id>/posts/', categories.category_posts, name='category_posts'),   
]