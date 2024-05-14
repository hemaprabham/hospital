from django import forms
from .models import Comment

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']  # Fields to be included in the form

    # Optionally, you can add custom validation methods for specific fields
    # For example, validating the email format
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email
