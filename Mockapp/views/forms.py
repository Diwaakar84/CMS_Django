from django import forms
from django.contrib.auth.models import User
from ..models import Post, Category
from django.contrib.auth.forms import UserCreationForm
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length = 20)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

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