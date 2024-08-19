from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'The e-mail must be valid'
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty',
                'max_length': 'This field must not have less then 5 chars',
                'invalid': 'This field is invalid'
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here',
                'class': 'input text-input '
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here',
            })
        }
