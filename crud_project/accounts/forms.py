from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    
    class Meta(UserCreationForm.Meta):
        Fields = ('username', 'email', 'password1', 'password2')
