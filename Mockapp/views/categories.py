from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'categories/show.html', {'category': category})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'categories/new.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST' and request.POST.get('_method') == 'patch':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to a view showing the list of categories or another appropriate page
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/edit.html', {'category': category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')
