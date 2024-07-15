from django.shortcuts import render, get_object_or_404, redirect
from ..models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})

def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(form)
        if form.is_valid():
            # Process form data if valid
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'categories/new.html', {'form': form})

def category_edit(request, pk):
    # Implement your edit view logic here
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/edit.html', {'category': category})

def category_delete(request, pk):
    # Implement your delete view logic here
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')
