from django.urls import path
from .views import HomeView, AboutView, ServiceView, MenuView, BookingView, OurTeamView, \
    TestimonialView, ContactView, CategoryView, TestView, ProductDetail


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('service', ServiceView.as_view(), name='service'),
    path('menu', MenuView.as_view(), name='menu'),
    path('booking', BookingView.as_view(), name='booking'),
    path('team', OurTeamView.as_view(), name='team'),
    path('testimonial', TestimonialView.as_view(), name='testimonial'),
    path('contact', ContactView.as_view(), name='contact'),
    path('category', CategoryView.as_view(), name='category'),
    path('test', TestView.as_view(), name='test'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
