from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username.')
        add_placeholder(self.fields['email'], 'Your e-mail.')
        add_placeholder(self.fields['first_name'], 'Ex.: James')
        add_placeholder(self.fields['last_name'], 'Ex.: Bond')
        add_placeholder(self.fields['password'], 'Type your password here')
        add_placeholder(self.fields['password2'], 'Repeat your password')
 
    username = forms.CharField(
        label='Username',
        help_text='Username must have letters, numbers or @/./+/-/_ and at least, 150 caracters.', # noqa E501
        error_messages={
                'required': 'This field is required.',
                'min_length': 'Ensure this value has at least 4 characters.',
                'max_length': 'Ensure this value has at most 150 characters.'
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Write your first name.'},
        label='First Name',
    )
    last_name = forms.CharField(
        error_messages={'required': 'Write your last name.'},
        label='Last Name',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
                'required': 'This field must not be empty.'
        },

        validators=[strong_password],
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
                'required': 'This field must not be empty.'
            },
        label='Password2'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
        help_text='The e-mail must be valid.',
        label='E-mail',
        error_messages={
                'required': 'The e-mail must be valid.'
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

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and Password2 must be equal',
                'password2': 'Password and Password2 must be equal',
            })
