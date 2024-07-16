from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .forms import UserUpdateForm

def welcome_index(request):
    return render(request, 'welcome/index.html')

# def sign_up(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/new.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome_index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'sessions/new.html')

def logout_view(request):
    logout(request)
    return redirect('welcome_index')

# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated!')
#             return redirect('edit_profile')
#     else:
#         form = UserUpdateForm(instance=request.user)
#     return render(request, 'users/edit.html', {'form': form})
