import form as form
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile


class RegisterForm(UserCreationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('profile_picture',)
