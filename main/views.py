from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Comment, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, TestForm
from django.db.models import Q
from datetime import datetime, timedelta


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        comments = Comment.objects.all()
        return render(request, 'index.html', {
            'products': products,
            'comments': comments
        })

    def post(self, request):
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        message = request.POST.get('message')

        comment = Comment.objects.create(
            name=name,
            profession=profession,
            message=message
        )
        comment.save()
        return redirect('/')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'service.html')


class MenuView(View):
    def get(self, request):
        products = Product.objects.all()
        products1 = Product.objects.filter(Q(price__gte=10) & Q(price__lte=30))
        products2 = Product.objects.filter(Q(title__icontains='salom') | Q(description__icontains='assalomu alaykum'))
        products3 = Product.objects.filter(Q(title__iexact='yaxshimisan') | Q(description__iexact='yaxshi rahmat'))
        date1 = datetime.now() - timedelta(hours=5)
        date2 = datetime.now()
        products4 = Product.objects.filter(Q(date__gt=date1) & Q(date__lt=date2)).order_by('-date')
        products5 = Product.objects.filter(Q(date__day=7) & Q(date__month=7) & Q(date__year=2023))
        return render(request, 'menu.html', {'products': products,})


class BookingView(View):
    def get(self, request):
        return render(request, 'booking.html')


class OurTeamView(View):
    def get(self, request):
        return render(request, 'team.html')


class TestimonialView(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        form = CommentForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            msg = f"""
    {message}
    Full Name: {name}
    email: {email}
    phone number: {phone}
            """
            send_mail(
                'Yangi xabar',
                msg,
                name,
                ['habibulloxayrullayev140@gmail.com'],
                fail_silently=True
            )
        return redirect('contact')


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category.html', {
            'categories': categories
        })

    def post(self, request):
        name = request.POST.get('name')
        category = Category.objects.create(
            name=name
        )
        category.save()
        return redirect('/')


class ProductDetail(View):
    def get(self, request, pk):
        products = Product.objects.get(pk=pk)
        return render(request, 'product_detail.html', {'products': products})


class TestView(View):
    def get(self, request):
        test = TestForm(request.POST)
        if test.is_valid():
            son1 = test.cleaned_data.get('son1')
            son2 = test.cleaned_data.get('son2')
            if son1 & son2 is not None:
                son3 = son1 + son2
                return render(request, 'test.html', {'son3': son3})
            else:
                return redirect('test')
        return redirect('test')
