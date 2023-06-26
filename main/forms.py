from django.forms import (
    Form,
    CharField,
    Textarea,
    TextInput,
    EmailField,
    EmailInput,
    IntegerField,
    NumberInput
)


class CommentForm(Form):
    name = CharField(label='name', widget=TextInput(attrs={
        'placeholder': 'Your Name',
        'id': 'name'
    }))
    email = EmailField(label='email', widget=EmailInput(attrs={
        'placeholder': 'Your Email',
        'id': 'email'
    }))
    phone = CharField(label='phone number', widget=TextInput(attrs={
        'placeholder': 'Phone number',
        'id': 'phone number'
    }))
    message = CharField(label='message', widget=Textarea(attrs={
        'placeholder': 'Leave a message here',
        'id': 'message'
    }))


class TestForm(Form):
    son1 = IntegerField(label='son1', widget=NumberInput(attrs={
        'placeholder': '1-sonni kiriting',
        'id': 'son1'
    }))
    son2 = IntegerField(label='son2', widget=NumberInput(attrs={
        'placeholder': '2-sonni kiriting',
        'id': 'son2'
    }))

