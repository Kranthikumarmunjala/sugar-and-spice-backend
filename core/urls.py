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



# # In core/urls.py

# from django.urls import path
# from django.contrib.auth import views as auth_views # Import Django's auth views
# from . import views

# # Defines the URL patterns for the core application
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





#     # Auth Views
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'), # New Logout URL

#     # Password Reset URLs (using Django's built-in views)
#     path('password-reset/', 
#          auth_views.PasswordResetView.as_view(template_name='core/forgot-password.html'), 
#          name='password_reset'),
#     path('password-reset/done/', 
#          auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), 
#          name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', 
#          auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), 
#          name='password_reset_confirm'),
#     path('password-reset-complete/', 
#          auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), 
#          name='password_reset_complete'),
# ]




# # In core/urls.py

# from django.urls import path
# from django.contrib.auth import views as auth_views # Import Django's auth views
# from . import views

# urlpatterns = [
#     # Page Views
#     path('', views.home_view, name='home'),
#     path('about/', views.about_view, name='about'),
#     path('menu/', views.menu_view, name='menu'),
#     path('order-online/', views.order_online_view, name='order-online'),
#     path('contact/', views.contact_view, name='contact'),
#     path('workshops/', views.workshops_view, name='workshops'),
#     path('cart/', views.cart_view, name='cart'),
#     path('booking-calendar/', views.booking_calendar_view, name='booking-calendar'),
#     path('booking-form/', views.booking_form_view, name='booking-form'),

#     # Auth Views
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),

#     # Password Reset URLs (using Django's built-in views)
#     # This replaces the old 'forgot-password/' URL
#     path('password-reset/', 
#          auth_views.PasswordResetView.as_view(template_name='core/forgot-password.html'), 
#          name='password_reset'),
#     path('password-reset/done/', 
#          auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), 
#          name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/', 
#          auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), 
#          name='password_reset_confirm'),
#     path('password-reset-complete/', 
#          auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), 
#          name='password_reset_complete'),
# ]




# In core/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views # Import Django's auth views
from . import views

urlpatterns = [
    # Page Views
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('order-online/', views.order_online_view, name='order-online'),
    path('contact/', views.contact_view, name='contact'),
    path('workshops/', views.workshops_view, name='workshops'),
    path('cart/', views.cart_view, name='cart'),
    path('booking-calendar/', views.booking_calendar_view, name='booking-calendar'),
    path('booking-form/', views.booking_form_view, name='booking-form'),

    # --- NEW: Payment URLs ---
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('payment-successful/', views.payment_successful, name='payment-successful'),
    path('payment-cancelled/', views.payment_cancelled, name='payment-cancelled'),

    # Auth Views
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Password Reset URLs (using Django's built-in views)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='core/forgot-password.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), 
         name='password_reset_complete'),
]