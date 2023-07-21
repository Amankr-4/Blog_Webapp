from django import forms
from .models import post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext ,gettext_lazy as _

class Signupform(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))  #dono password fields models ke ander nhi aate ye forms ke part h thats way isko alag se yaha likhna parta h
    password2 = forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name' : 'First Name', 'last_name' : 'Last Name','email' : 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.TextInput(attrs={'class':'form-control'})}

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))        

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields= ['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        