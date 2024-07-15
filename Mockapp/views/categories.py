from django.shortcuts import render, get_object_or_404, redirect
from ..models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})

def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

def category_create(request):
    # Implement your create view logic here
    return render(request, 'categories/new.html')

def category_edit(request, pk):
    # Implement your edit view logic here
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/edit.html', {'category': category})

def category_delete(request, pk):
    # Implement your delete view logic here
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')
