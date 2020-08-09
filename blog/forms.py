
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from  django import forms
from django.contrib.auth.models import User
from blog.models import Post

from django.utils.translation import gettext, gettext_lazy as _




class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title', 'description']
        widgets= {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'write title heree'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'write title description','cols':5,'rows':5}),
        }







class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Again',widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=  User
        fields = ['username','email']  
        labels ={'email':'Email address'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
           }
        

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
      label=_("Password"),
           strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class classname(object):
    pass