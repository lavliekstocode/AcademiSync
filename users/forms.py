from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.USER_ROLES, widget=forms.Select())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'school', 'resume', 'password1', 'password2']

from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["title", "file"]


