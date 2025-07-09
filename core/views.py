# In core/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')

def menu_view(request):
    return render(request, 'core/menu.html')

def order_online_view(request):
    return render(request, 'core/order-online.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def workshops_view(request):
    return render(request, 'core/workshops.html')

def login_view(request):
    return render(request, 'core/login.html')

def signup_view(request):
    return render(request, 'core/signup.html')

def forgot_password_view(request):
    # Renamed the file to avoid conflicts with Django's built-in 'forgot-password'
    return render(request, 'core/forgot-password.html')

def cart_view(request):
    return render(request, 'core/cart.html')

def booking_calendar_view(request):
    return render(request, 'core/booking-calendar.html')

def booking_form_view(request):
    return render(request, 'core/booking-form.html')