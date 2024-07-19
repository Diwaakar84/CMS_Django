from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from ..models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    return render(request, 'posts/show.html', {'post': post})

@login_required
def user_posts(request, user_id):
    posts = Post.objects.filter(user=user_id)
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('post_index')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_index')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit.html', {'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    post.delete()
    return redirect('post_index')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save()

    return redirect('post_detail', pk=post_id)

@login_required
def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)

    if request.user == comment.commenter or request.user == post.user:
        comment.delete()
    else:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    return redirect('post_detail', pk=post_id)