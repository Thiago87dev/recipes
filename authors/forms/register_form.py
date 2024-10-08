from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_form_utils import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['first_name'], 'Your first name')
        add_placeholder(self.fields['last_name'], 'Your last name')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['password'], 'Your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    username = forms.CharField(
        label='Username',
        help_text='Username must have letters, numbers or one of those @.+-_. '
        'The length should be between 4 and 150 characters.',
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters'
        },
        min_length=4,
        max_length=150,
    )

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least 1 uppercase letter, 1 lowercase letter and 1 number. '
            'The length should be at least 8 chars.'
        ),
        validators=[strong_password],
        label='Password'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Repeat your password',
        error_messages={
            'required': 'Please, repeat your password'
        },
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

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError('E-mail is already in use', code='invalid')

        return email

    def clean(self):
        clened_data = super().clean()

        password = clened_data.get('password')
        password2 = clened_data.get('password2')

        if password != password2:
            password_validation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )

            raise ValidationError({
                'password': password_validation_error,
                'password2': [
                    password_validation_error
                ]
            })
