from django.shortcuts import render, get_object_or_404, redirect
from ..models import Post

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})

def new_post(request):
    # Implement your create view logic here
    return render(request, 'posts/new.html')

def post_edit(request, pk):
    # Implement your edit view logic here
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/edit.html', {'post': post})

def post_delete(request, pk):
    # Implement your delete view logic here
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
