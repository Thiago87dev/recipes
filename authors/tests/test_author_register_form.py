from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('first_name', 'Your first name'),
        ('last_name', 'Your last name'),
        ('email', 'Your e-mail'),
        ('password', 'Your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, current_placeholder)

    @parameterized.expand([
        ('username', 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
        ('email', 'The e-mail must be valid'),
        ('password', (
            'Password must have at least 1 uppercase letter, 1 lowercase letter and 1 number. '
            'The length should be at least 8 chars.'
        )),
    ])
    def test_fields_help_text_is_correct(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(needed, current)

    @parameterized.expand([
        ('username', 'Username'),
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_label_is_correct(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(needed, current)
