

# # In core/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .models import (
#     BaseConfig, HomePageImage, HomeLinks, AboutConfig,
#     MenuConfig, MenuItems, OrderConfig, OrderItems, ContactConfig,
#     Contact, WorkConfig, Workshop, Booking, Cart, CustomUser,ScheduleConfig
# )
# from datetime import datetime, time
# import calendar


# def get_available_slots(request):
#     """
#     API endpoint to fetch available slots for a given month and year.
#     Returns a JSON object with available dates.
#     Example request: /api/available-slots/?year=2025&month=7
#     """
#     year = int(request.GET.get('year'))
#     month = int(request.GET.get('month'))
    
#     # Define all possible time slots from 10 AM to 5 PM
#     all_time_slots = [
#         time(10, 0), time(11, 0), time(12, 0),
#         time(13, 0), time(14, 0), time(15, 0),
#         time(16, 0), time(17, 0)
#     ]
    
#     # Get all bookings for the given month and year
#     bookings = Booking.objects.filter(
#         booking_date__year=year,
#         booking_date__month=month
#     )
    
#     availability = {}
    
#     # Get the number of days in the month
#     num_days = calendar.monthrange(year, month)[1]

#     for day in range(1, num_days + 1):
#         # Create a date object for the current day
#         current_date = datetime(year, month, day).date()
        
#         # Skip past dates
#         if current_date < datetime.today().date():
#             continue

#         # Get bookings for this specific day
#         day_bookings = bookings.filter(booking_date=current_date)
#         booked_times = [b.booking_time for b in day_bookings]
        
#         # Find which of the all_time_slots are NOT booked
#         available_slots_for_day = [
#             t.strftime("%I:%M %p").strip() for t in all_time_slots if t not in booked_times
#         ]
        
#         # If there are any available slots, add the date to our availability dict
#         if available_slots_for_day:
#             date_str = current_date.strftime('%Y-%m-%d')
#             availability[date_str] = available_slots_for_day
            
#     return JsonResponse(availability)



# # --- BASE CONTEXT (Remains the same) ---
# def get_base_context():
#     return {'base_config': BaseConfig.objects.first()}

# # --- AUTHENTICATION VIEWS ---

# def signup_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         first_name = request.POST.get('first-name')
#         last_name = request.POST.get('last-name')

#         if not email or not password:
#             messages.error(request, 'Email and password are required.')
#             return render(request, 'core/signup.html', get_base_context())

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, 'An account with this email already exists.')
#             return render(request, 'core/signup.html', get_base_context())

#         user = CustomUser.objects.create_user(username=email, email=email, password=password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()

#         login(request, user)
#         messages.success(request, 'Account created successfully! You are now logged in.')
#         return redirect('home')
    
#     return render(request, 'core/signup.html', get_base_context())

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')
        
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Welcome back, {user.first_name or user.username}!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid email or password.')

#     return render(request, 'core/login.html', get_base_context())

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been successfully logged out.')
#     return redirect('home')

# # --- CART VIEW ---

# def cart_view(request):
#     context = get_base_context()
#     cart_items = []
#     subtotal = 0
#     if request.user.is_authenticated:
#         cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
#         subtotal = sum(item.quantity * item.item.price for item in cart_items)
    
#     context.update({
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#     })
#     return render(request, 'core/cart.html', context)


# # --- OTHER PAGE VIEWS (Unchanged, provided for completeness) ---

# # def home_view(request):
# #     context = get_base_context()
# #     context.update({
# #         'slides': HomeConfig.objects.all(),
# #         'gallery_images': HomeImages.objects.all(),
# #         'social_links': HomeLinks.objects.first(),
# #     })
# #     return render(request, 'core/index.html', context)


# # In core/views.py
# def home_view(request):
#     context = get_base_context()
#     context.update({
#         # Pass the queryset under a single, clear name
#         'home_images': HomePageImage.objects.all(),
#         'social_links': HomeLinks.objects.first(),
#     })
#     return render(request, 'core/index.html', context)

# def about_view(request):
#     context = get_base_context()
#     context.update({'about_config': AboutConfig.objects.first()})
#     return render(request, 'core/about.html', context)

# def menu_view(request):
#     context = get_base_context()
#     context.update({
#         'menu_config': MenuConfig.objects.first(),
#         'menu_items': MenuItems.objects.all(),
#     })
#     return render(request, 'core/menu.html', context)

# def order_online_view(request):
#     context = get_base_context()
#     context.update({
#         'order_config': OrderConfig.objects.first(),
#         'order_items': OrderItems.objects.all(),
#     })
#     return render(request, 'core/order-online.html', context)

# # def contact_view(request):
# #     if request.method == 'POST':
# #         Contact.objects.create(
# #             first_name=request.POST.get('first-name'),
# #             last_name=request.POST.get('last-name'),
# #             email=request.POST.get('email'),
# #             phone=request.POST.get('phone'),
# #             message=request.POST.get('message'),
# #         )
# #         return redirect('contact')
# #     context = get_base_context()
# #     context.update({'contact_config': ContactConfig.objects.first()})
# #     return render(request, 'core/contact.html', context)


# def contact_view(request):
#     if request.method == 'POST':
#         Contact.objects.create(
#             first_name=request.POST.get('first-name'),
#             last_name=request.POST.get('last-name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             message=request.POST.get('message'),
#         )
#         # Add a success message to be displayed on the next page render
#         messages.success(request, 'Thank you! Your message has been sent successfully.')
#         return redirect('contact') # Redirect to the same page (to prevent re-submission)

#     context = get_base_context()
#     context.update({
#         'contact_config': ContactConfig.objects.first(),
#     })
#     return render(request, 'core/contact.html', context)

# def workshops_view(request):
#     context = get_base_context()
#     context.update({
#         'work_config': WorkConfig.objects.first(),
#         'workshops': Workshop.objects.all(),
#     })
#     return render(request, 'core/workshops.html', context)

# def booking_calendar_view(request):
#     context = get_base_context()
#     context.update({'schedule_config': ScheduleConfig.objects.first()})
#     return render(request, 'core/booking-calendar.html', context)

# def booking_form_view(request):
#     if request.method == 'POST':
#         Booking.objects.create(
#             first_name=request.POST.get('first-name'),
#             last_name=request.POST.get('last-name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             message=request.POST.get('message'),
#         )
#         return redirect('home')
#     return render(request, 'core/booking-form.html', get_base_context())



# In core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .models import (
    TitleConfig, HomePageImage, MenuItems, OrderItems, Contact, 
    Workshop, Booking, Cart, CustomUser
)
from datetime import datetime, time
import calendar

# --- NEW BASE CONTEXT ---
# This function now fetches the single TitleConfig object for all pages.
def get_site_context():
    """
    Fetches the single TitleConfig object to be used as context across the site.
    """
    return {'site_config': TitleConfig.objects.first()}

# --- API VIEW (Unchanged Logic, but added import for JsonResponse) ---
def get_available_slots(request):
    """
    API endpoint to fetch available slots for a given month and year.
    Returns a JSON object with available dates.
    Example request: /api/available-slots/?year=2025&month=7
    """
    year = int(request.GET.get('year'))
    month = int(request.GET.get('month'))
    
    all_time_slots = [
        time(10, 0), time(11, 0), time(12, 0),
        time(13, 0), time(14, 0), time(15, 0),
        time(16, 0), time(17, 0)
    ]
    
    bookings = Booking.objects.filter(booking_date__year=year, booking_date__month=month)
    availability = {}
    num_days = calendar.monthrange(year, month)[1]

    for day in range(1, num_days + 1):
        current_date = datetime(year, month, day).date()
        if current_date < datetime.today().date():
            continue

        day_bookings = bookings.filter(booking_date=current_date)
        booked_times = [b.booking_time for b in day_bookings]
        
        available_slots_for_day = [
            t.strftime("%I:%M %p").strip() for t in all_time_slots if t not in booked_times
        ]
        
        if available_slots_for_day:
            date_str = current_date.strftime('%Y-%m-%d')
            availability[date_str] = available_slots_for_day
            
    return JsonResponse(availability)


# --- AUTHENTICATION VIEWS (Logic is the same, just context method changes) ---

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')

        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return render(request, 'core/signup.html', get_site_context())

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'core/signup.html', get_site_context())

        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        login(request, user)
        messages.success(request, 'Account created successfully! You are now logged in.')
        return redirect('home')
    
    return render(request, 'core/signup.html', get_site_context())

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'core/login.html', get_site_context())

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

# --- CART VIEW (Logic is the same, just context method changes) ---

def cart_view(request):
    context = get_site_context()
    cart_items = []
    subtotal = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
        subtotal = sum(item.quantity * item.item.price for item in cart_items)
    
    context.update({
        'cart_items': cart_items,
        'subtotal': subtotal,
    })
    return render(request, 'core/cart.html', context)

# --- PAGE VIEWS (Updated to use the new context and models) ---

def home_view(request):
    context = get_site_context()
    context.update({
        'home_images': HomePageImage.objects.all(),
    })
    return render(request, 'core/index.html', context)

def about_view(request):
    context = get_site_context()
    # No extra context needed, all data is in site_config
    return render(request, 'core/about.html', context)

def menu_view(request):
    context = get_site_context()
    context.update({
        'menu_items': MenuItems.objects.all(),
    })
    return render(request, 'core/menu.html', context)

def order_online_view(request):
    context = get_site_context()
    context.update({
        'order_items': OrderItems.objects.all(),
    })
    return render(request, 'core/order-online.html', context)

def contact_view(request):
    context = get_site_context()
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first-name'),
            last_name=request.POST.get('last-name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Thank you! Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'core/contact.html', context)

def workshops_view(request):
    context = get_site_context()
    context.update({
        'workshops': Workshop.objects.all(),
    })
    return render(request, 'core/workshops.html', context)

def booking_calendar_view(request):
    context = get_site_context()
    # No extra context needed, all data is in site_config
    return render(request, 'core/booking-calendar.html', context)

def booking_form_view(request):
    context = get_site_context()
    if request.method == 'POST':
        # This part assumes booking details are passed somehow (e.g., via session or form)
        # The logic here remains simple as per original code.
        Booking.objects.create(
            first_name=request.POST.get('first-name'),
            last_name=request.POST.get('last-name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Your workshop has been booked successfully!')
        return redirect('home')
        
    return render(request, 'core/booking-form.html', context)