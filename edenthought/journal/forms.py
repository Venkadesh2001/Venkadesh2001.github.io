from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import CreateThought,Profile
from django.forms.widgets import TextInput,PasswordInput,FileInput




class Create_Thought(ModelForm):
    class Meta:
        model = CreateThought
        fields = ['title','description',]


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password =forms.CharField(widget = PasswordInput())


class UpdateUserForm(forms.ModelForm):
    password  = None
    class Meta:
        model = User
        fields = ['username','email',]
        
        exclude = ['password1','password2',]


class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs = {'class':'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['profile_pic']




