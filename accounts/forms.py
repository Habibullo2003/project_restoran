from django.forms import (
    Form, CharField, TextInput, EmailField, EmailInput, PasswordInput
)


class RegisterForm(Form):
    first_name = CharField(label='first_name', widget=TextInput(attrs={
        'placeholder': 'First_name',
        'id': 'first_name',
    }))
    last_name = CharField(label='last_name', widget=TextInput(attrs={
        'placeholder': 'Last_name',
        'id': 'last_name',
    }))
    email = EmailField(label='email', widget=EmailInput(attrs={
        'placeholder': 'Email',
        'id': 'email',
    }))
    username = CharField(label='username', widget=TextInput(attrs={
        'placeholder': 'Username',
        'id': 'username'
    }))
    password = CharField(label='password', widget=PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password'
    }))
    password_confirm = CharField(label='password_confirm', widget=PasswordInput(attrs={
        'placeholder': 'Password_confirm',
        'id': 'password_confirm'
    }))


class LoginForm(Form):
    username = CharField(label='username', widget=TextInput(attrs={
        'placeholder': 'Username',
        'id': 'username'
    }))
    password = CharField(label='password', widget=PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password'
    }))
