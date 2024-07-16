from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = render("user/sign_up.html")
    return render(request, 'user/sign_up.html', {'form': form, 'title':'register here'})

def Login(request):
    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

# class SignUpView(CreateView):
#     template_name = 'registration/sign_up.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('welcome_index')

#     def form_valid(self, form):
#         # Save the user and log them in
#         print(self)
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('welcome_index')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'sessions/new.html')

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
