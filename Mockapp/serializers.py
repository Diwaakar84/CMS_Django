# from rest_framework import serializers
# from .models import User, Post, Category, Comment, Like

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'created_at', 'updated_at']

# class PostSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'description', 'categories', 'user', 'created_at', 'updated_at']

# class CategorySerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'posts',    'created_at', 'updated_at']

# class CommentSerializer(serializers.ModelSerializer):
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Comment
#         fields = ['id', 'commenter', 'text', 'post', 'user', 'created_at', 'updated_at']

# class LikeSerializer(serializers.ModelSerializer):
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Like
#         fields = ['id', 'post', 'user', 'created_at', 'updated_at']