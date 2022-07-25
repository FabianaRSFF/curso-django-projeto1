import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter,'
            ' one lowercase letter and one number. At least '
            '8 characters.'
        ),
            code='Invalid'
        )


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
        help_text=('Username must have letters, numbers or @/./+/-/_ and at least, 150 characters.'), # noqa E501
        error_messages={
                'required': 'This field must not be empty.',
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
       
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': "Passwords doesn't match",
                'password2': "Passwords doesn't match",
            })
