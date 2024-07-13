from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CategoryViewSet, CommentViewSet, LikeViewSet
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sign_up/', UserViewSet.as_view({'post': 'create'}), name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/', UserViewSet.as_view({'patch': 'partial_update'}), name='edit_profile'),
    path('welcome/index/', TemplateView.as_view(template_name='welcome/index.html'), name='welcome'),
    path('users/<int:user_id>/my_posts/', PostViewSet.as_view({'get': 'list'}), name='my_posts'),
    path('categories/<int:category_id>/posts/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category_posts'),
    path('not_found/', TemplateView.as_view(template_name='404.html'), name='page_not_found'),
]