# # In core/urls.py (new file)

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('about/', views.about_view, name='about'),
#     path('menu/', views.menu_view, name='menu'),
#     path('order-online/', views.order_online_view, name='order-online'),
#     path('contact/', views.contact_view, name='contact'),
#     path('workshops/', views.workshops_view, name='workshops'),
#     path('login/', views.login_view, name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('forgot-password/', views.forgot_password_view, name='forgot-password'),
#     path('cart/', views.cart_view, name='cart'),
#     path('booking-calendar/', views.booking_calendar_view, name='booking-calendar'),
#     path('booking-form/', views.booking_form_view, name='booking-form'),
# ]



# In core/urls.py

from django.urls import path
from . import views

# Defines the URL patterns for the core application
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('order-online/', views.order_online_view, name='order-online'),
    path('contact/', views.contact_view, name='contact'),
    path('workshops/', views.workshops_view, name='workshops'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('cart/', views.cart_view, name='cart'),
    path('booking-calendar/', views.booking_calendar_view, name='booking-calendar'),
    path('booking-form/', views.booking_form_view, name='booking-form'),
]