from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import RegisterForm, LoginForm
from django.views import View


class Register(View):
    def register(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                password_confirm = form.cleaned_data.get('password_confirm')

                if password == password_confirm:
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'Username already exists! Please enter another username.')
                        return redirect('register')
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email already exists! Please enter another email.')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            username=username,
                            password=password
                        )
                        user.save()
                        return redirect('/')
                else:
                    messages.error(request, 'Passwords are not same')
                    return redirect('register')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})


class Login(View):
    def login(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Username or password is invalid!')
                    return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})


class Logout(View):
    def logout(self, request):
        auth.logout(request)
        return redirect('/')
