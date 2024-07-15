from django import forms
from django.contrib.auth.models import User
from ..models import Post, Category
from django.contrib.auth.forms import UserCreationForm
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length = 20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        
    # Additional customization if needed
    # category_ids = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']