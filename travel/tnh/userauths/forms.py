from django import forms 
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile 

class UserRegisterForm(UserCreationForm):
    full_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter full name", 'class':'custom class'}))
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter usernae", 'class':'custom class'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter email", 'class':'custom class'}))
    #password1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter the password", 'class':'custom class'}))
    #password2= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Confirm the password", 'class':'custom class'}))

    class Meta:
        
        model = User
        fields = ['full_name', 'username', 'email','phone', 'password1', 'password2']
        


