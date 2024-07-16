from django.shortcuts import render, get_object_or_404, redirect
from ..models import Post
from .forms import PostForm

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():

            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {'form': form})

def post_edit(request, pk):
    # Implement your edit view logic here
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/edit.html', {'post': post})

def post_delete(request, pk):
    # Implement your delete view logic here
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
