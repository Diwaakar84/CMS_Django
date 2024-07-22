from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from ..models import Post, Comment
from .forms import PostForm, CommentForm
from django.conf import settings
from django.db import router

def post_index(request):
    posts = []
    shards = getattr(settings, 'DATABASES', {}).keys()
    for shard in shards:
        posts.extend(Post.objects.using(shard).all())
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    post = None
    for shard in ['shard1', 'shard2', 'shard3']:
        try:
            post = Post.objects.using(shard).get(pk=pk)
            break
        except Post.DoesNotExist:
            continue
    if not post:
        raise Http404("Post does not exist")
    
    form = CommentForm()
    return render(request, 'posts/show.html', {'post': post})

@login_required
def user_posts(request, user_id):
    posts = Post.objects.using('default').filter(user=user_id)
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            shard = router.db_for_write(post.__class__, user_id=post.user.id)
            post.save(using=shard)

            return redirect('post_index')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = None
    for shard in ['shard1', 'shard2', 'shard3']:
        try:
            post = Post.objects.using(shard).get(pk=pk)
            break
        except Post.DoesNotExist:
            continue
    if not post:
        raise Http404("Post does not exist")

    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():

            form.save(using=shard)
            return redirect('post_index')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'posts/edit.html', {'post': post})

@login_required
def post_delete(request, pk):
    post = None
    for shard in ['shard1', 'shard2', 'shard3']:
        try:
            post = Post.objects.using(shard).get(pk=pk)
            break
        except Post.DoesNotExist:
            continue
    if not post:
        raise Http404("Post does not exist")

    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    post.delete(using=shard)
    return redirect('post_index')

@login_required
def add_comment(request, post_id):
    post = None
    for shard in ['shard1', 'shard2', 'shard3']:
        try:
            post = Post.objects.using(shard).get(pk=post_id)
            break
        except Post.DoesNotExist:
            continue
    if not post:
        raise Http404("Post does not exist")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.commenter = request.user
            comment.save(using='default')

    return redirect('post_detail', pk=post_id)

@login_required
def delete_comment(request, post_id, comment_id):
    post = None
    for shard in ['shard1', 'shard2', 'shard3']:
        try:
            post = Post.objects.using(shard).get(pk=post_id)
            break
        except Post.DoesNotExist:
            continue
    if not post:
        raise Http404("Post does not exist")
    
    comment = get_object_or_404(Comment.objects.using('default'), id=comment_id, post_id=post_id)

    if request.user == comment.commenter or request.user == post.user:
        comment.delete(using='default')  # Delete using the default database
    else:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    return redirect('post_detail', pk=post_id)