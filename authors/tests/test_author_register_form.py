from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username.'),
        ('email', 'Your e-mail.'),
        ('first_name', 'Ex.: James'),
        ('last_name', 'Ex.: Bond'),
        ('password', 'Type your password here'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
    
    @parameterized.expand([
        ('username', (
                    'Obrigatório. 150 caracteres ou menos.'
                    ' Letras, números e @/./+/-/_ apenas.')),
        ('email', ''),
        ('password', (
            'Password must have at least one uppercase letter,'
            ' one lowercase letter and one number. At least '
            '8 characters.'
        )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)