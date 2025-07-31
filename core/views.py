

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








# # In core/views.py

# # from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, login, logout
# # from django.contrib import messages
# # from django.http import JsonResponse
# # from .models import (
# #     TitleConfig, HomePageImage, MenuItems, OrderItems, Contact, 
# #     Workshop, Booking, Cart, CustomUser
# # )
# # from datetime import datetime, time
# # import calendar

# # --- NEW BASE CONTEXT ---
# # This function now fetches the single TitleConfig object for all pages.
# def get_site_context():
#     """
#     Fetches the single TitleConfig object to be used as context across the site.
#     """
#     return {'site_config': TitleConfig.objects.first()}

# # --- API VIEW (Unchanged Logic, but added import for JsonResponse) ---
# def get_available_slots(request):
#     """
#     API endpoint to fetch available slots for a given month and year.
#     Returns a JSON object with available dates.
#     Example request: /api/available-slots/?year=2025&month=7
#     """
#     year = int(request.GET.get('year'))
#     month = int(request.GET.get('month'))
    
#     all_time_slots = [
#         time(10, 0), time(11, 0), time(12, 0),
#         time(13, 0), time(14, 0), time(15, 0),
#         time(16, 0), time(17, 0)
#     ]
    
#     bookings = Booking.objects.filter(booking_date__year=year, booking_date__month=month)
#     availability = {}
#     num_days = calendar.monthrange(year, month)[1]

#     for day in range(1, num_days + 1):
#         current_date = datetime(year, month, day).date()
#         if current_date < datetime.today().date():
#             continue

#         day_bookings = bookings.filter(booking_date=current_date)
#         booked_times = [b.booking_time for b in day_bookings]
        
#         available_slots_for_day = [
#             t.strftime("%I:%M %p").strip() for t in all_time_slots if t not in booked_times
#         ]
        
#         if available_slots_for_day:
#             date_str = current_date.strftime('%Y-%m-%d')
#             availability[date_str] = available_slots_for_day
            
#     return JsonResponse(availability)


# # --- AUTHENTICATION VIEWS (Logic is the same, just context method changes) ---

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
#             return render(request, 'core/signup.html', get_site_context())

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, 'An account with this email already exists.')
#             return render(request, 'core/signup.html', get_site_context())

#         user = CustomUser.objects.create_user(username=email, email=email, password=password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()

#         login(request, user)
#         messages.success(request, 'Account created successfully! You are now logged in.')
#         return redirect('home')
    
#     return render(request, 'core/signup.html', get_site_context())


# # In core/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required # <-- Add this import
# from django.http import JsonResponse
# from django.conf import settings # <-- Add this import
# import stripe # <-- Add this import

# from .models import (
#     TitleConfig, HomePageImage, MenuItems, OrderItems, Contact, 
#     Workshop, Booking, Cart, CustomUser,
#     Order, OrderItem # <-- Add these imports
# )
# from datetime import datetime, time
# import calendar

# # --- NEW: Stripe API Key Configuration ---
# stripe.api_key = settings.STRIPE_SECRET_KEY

# # ... (keep get_site_context, get_available_slots, signup_view) ...

# def login_view(request):
#     # --- MODIFICATION START ---
#     # Prevent another user from logging in if one is already authenticated
#     if request.user.is_authenticated:
#         messages.error(request, f'User "{request.user.username}" is already logged in. Please log out first.')
#         return redirect('home')
#     # --- MODIFICATION END ---
        
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

#     return render(request, 'core/login.html', get_site_context())


# # def login_view(request):
# #     if request.user.is_authenticated:
# #         return redirect('home')
        
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')

# #         user = authenticate(request, username=email, password=password)

# #         if user is not None:
# #             login(request, user)
# #             messages.success(request, f'Welcome back, {user.first_name or user.username}!')
# #             return redirect('home')
# #         else:
# #             messages.error(request, 'Invalid email or password.')

# #     return render(request, 'core/login.html', get_site_context())

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been successfully logged out.')
#     return redirect('home')

# # --- CART VIEW (Logic is the same, just context method changes) ---

# # def cart_view(request):
# #     context = get_site_context()
# #     cart_items = []
# #     subtotal = 0
# #     if request.user.is_authenticated:
# #         cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
# #         subtotal = sum(item.quantity * item.item.price for item in cart_items)
    
# #     context.update({
# #         'cart_items': cart_items,
# #         'subtotal': subtotal,
# #     })
# #     return render(request, 'core/cart.html', context)



# @login_required
# def cart_view(request):
#     context = get_site_context()
#     cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    
#     # --- MODIFICATION START ---
#     # Calculate totals and add them to the cart_items queryset
#     # This makes the data available in the template
#     cart_items_with_totals = []
#     subtotal = 0
#     for item in cart_items:
#         item.line_total = item.quantity * item.item.price
#         subtotal += item.line_total
#         cart_items_with_totals.append(item)
#     # --- MODIFICATION END ---
    
#     context.update({
#         # Use the new list which includes the line_total
#         'cart_items': cart_items_with_totals, 
#         'subtotal': subtotal,
#     })
#     return render(request, 'core/cart.html', context)

# # @login_required # <-- Add this decorator
# # def cart_view(request):
# #     context = get_site_context()
# #     # This filter ensures only the logged-in user's cart is fetched.
# #     cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
# #     subtotal = sum(item.quantity * item.item.price for item in cart_items)
    
# #     context.update({
# #         'cart_items': cart_items,
# #         'subtotal': subtotal,
# #     })
# #     return render(request, 'core/cart.html', context)

# # --- PAGE VIEWS (Updated to use the new context and models) ---

# def home_view(request):
#     context = get_site_context()
#     context.update({
#         'home_images': HomePageImage.objects.all(),
#     })
#     return render(request, 'core/index.html', context)

# def about_view(request):
#     context = get_site_context()
#     # No extra context needed, all data is in site_config
#     return render(request, 'core/about.html', context)

# def menu_view(request):
#     context = get_site_context()
#     context.update({
#         'menu_items': MenuItems.objects.all(),
#     })
#     return render(request, 'core/menu.html', context)

# def order_online_view(request):
#     context = get_site_context()
#     context.update({
#         'order_items': OrderItems.objects.all(),
#     })
#     return render(request, 'core/order-online.html', context)

# def contact_view(request):
#     context = get_site_context()
#     if request.method == 'POST':
#         Contact.objects.create(
#             first_name=request.POST.get('first-name'),
#             last_name=request.POST.get('last-name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             message=request.POST.get('message'),
#         )
#         messages.success(request, 'Thank you! Your message has been sent successfully.')
#         return redirect('contact')

#     return render(request, 'core/contact.html', context)

# def workshops_view(request):
#     context = get_site_context()
#     context.update({
#         'workshops': Workshop.objects.all(),
#     })
#     return render(request, 'core/workshops.html', context)

# def booking_calendar_view(request):
#     context = get_site_context()
#     # No extra context needed, all data is in site_config
#     return render(request, 'core/booking-calendar.html', context)

# def booking_form_view(request):
#     context = get_site_context()
#     if request.method == 'POST':
#         # This part assumes booking details are passed somehow (e.g., via session or form)
#         # The logic here remains simple as per original code.
#         Booking.objects.create(
#             first_name=request.POST.get('first-name'),
#             last_name=request.POST.get('last-name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             message=request.POST.get('message'),
#         )
#         messages.success(request, 'Your workshop has been booked successfully!')
#         return redirect('home')
        
#     return render(request, 'core/booking-form.html', context)



# @login_required
# def create_checkout_session(request):
#     cart_items = Cart.objects.filter(user=request.user)
    
#     if not cart_items:
#         messages.error(request, "Your cart is empty.")
#         return redirect('cart')

#     line_items = []
#     for cart_item in cart_items:
#         line_items.append({
#             'price_data': {
#                 'currency': 'aud',
#                 'product_data': {
#                     'name': cart_item.item.name,
#                     'images': [f"{settings.SITE_URL}{cart_item.item.image.url}" if cart_item.item.image else None],
#                 },
#                 'unit_amount': int(cart_item.item.price * 100), # Price in cents
#             },
#             'quantity': cart_item.quantity,
#         })

#     try:
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=line_items,
#             mode='payment',
#             customer_email=request.user.email, # Pre-fill email
#             success_url=settings.SITE_URL + '/payment-successful/?session_id={CHECKOUT_SESSION_ID}',
#             cancel_url=settings.SITE_URL + '/payment-cancelled/',
#             metadata={
#                 'user_id': request.user.id
#             }
#         )
#         return redirect(checkout_session.url, code=303)
#     except Exception as e:
#         messages.error(request, f"Something went wrong with the payment gateway. {str(e)}")
#         return redirect('cart')


# @login_required
# def payment_successful(request):
#     context = get_site_context()
#     session_id = request.GET.get('session_id')
    
#     if not session_id:
#         messages.error(request, "Invalid request for payment success.")
#         return redirect('home')

#     try:
#         session = stripe.checkout.Session.retrieve(session_id)
#         payment_intent = stripe.PaymentIntent.retrieve(session.payment_intent)
        
#         # Check if order already exists
#         if Order.objects.filter(stripe_payment_intent=payment_intent.id).exists():
#             messages.info(request, "This order has already been processed.")
#             return render(request, 'core/payment_successful.html', context)

#         # Create Order
#         order = Order.objects.create(
#             user=request.user,
#             first_name=request.user.first_name,
#             last_name=request.user.last_name,
#             email=request.user.email,
#             total_paid=session.amount_total / 100, # Convert from cents to dollars
#             stripe_payment_intent=payment_intent.id,
#             is_paid=True
#         )

#         # Get cart items and create OrderItems
#         cart_items = Cart.objects.filter(user=request.user)
#         for cart_item in cart_items:
#             OrderItem.objects.create(
#                 order=order,
#                 item=cart_item.item,
#                 quantity=cart_item.quantity,
#                 price=cart_item.item.price # Save price at time of purchase
#             )

#         # Clear the user's cart
#         cart_items.delete()

#         messages.success(request, "Payment Successful! Your order has been placed.")
#         return render(request, 'core/payment_successful.html', context)

#     except stripe.error.StripeError as e:
#         messages.error(request, f"There was an error processing your payment: {str(e)}")
#         return redirect('home')
#     except Exception as e:
#         messages.error(request, f"An unexpected error occurred: {str(e)}")
#         return redirect('home')


# def payment_cancelled(request):
#     context = get_site_context()
#     messages.error(request, "Your payment was cancelled. You have not been charged.")
#     return render(request, 'core/payment_cancelled.html', context)












### `core/views.py`
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required # <-- Add this import
from django.http import JsonResponse
from django.conf import settings # <-- Add this import
import stripe # <-- Add this import

from .models import (
    TitleConfig, HomePageImage, MenuItems, OrderItems, Contact, 
    Workshop, Booking, Cart, CustomUser,
    Order, OrderItem # <-- Add these imports
)
from datetime import datetime, time
import calendar

# --- NEW: Stripe API Key Configuration ---
stripe.api_key = settings.STRIPE_SECRET_KEY

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


# ... (keep get_site_context, get_available_slots, signup_view) ...

def login_view(request):
    # --- MODIFICATION START ---
    # Prevent another user from logging in if one is already authenticated
    if request.user.is_authenticated:
        messages.error(request, f'User "{request.user.username}" is already logged in. Please log out first.')
        return redirect('home')
    # --- MODIFICATION END ---
        
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

#     return render(request, 'core/login.html', get_site_context())

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

# --- CART VIEW (Logic is the same, just context method changes) ---

# def cart_view(request):
#     context = get_site_context()
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



@login_required
def cart_view(request):
    context = get_site_context()
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    
    # --- MODIFICATION START ---
    # Calculate totals and add them to the cart_items queryset
    # This makes the data available in the template
    cart_items_with_totals = []
    subtotal = 0
    for item in cart_items:
        item.line_total = item.quantity * item.item.price
        subtotal += item.line_total
        cart_items_with_totals.append(item)
    # --- MODIFICATION END ---
    
    context.update({
        # Use the new list which includes the line_total
        'cart_items': cart_items_with_totals, 
        'subtotal': subtotal,
    })
    return render(request, 'core/cart.html', context)

# @login_required # <-- Add this decorator
# def cart_view(request):
#     context = get_site_context()
#     # This filter ensures only the logged-in user's cart is fetched.
#     cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
#     subtotal = sum(item.quantity * item.item.price for item in cart_items)
    
#     context.update({
#         'cart_items': cart_items,
#         'subtotal': subtotal,
#     })
#     return render(request, 'core/cart.html', context)

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



@login_required
def create_checkout_session(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    line_items = []
    for cart_item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'aud',
                'product_data': {
                    'name': cart_item.item.name,
                    'images': [f"{settings.SITE_URL}{cart_item.item.image.url}" if cart_item.item.image else None],
                },
                'unit_amount': int(cart_item.item.price * 100), # Price in cents
            },
            'quantity': cart_item.quantity,
        })

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            customer_email=request.user.email, # Pre-fill email
            success_url=settings.SITE_URL + '/payment-successful/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.SITE_URL + '/payment-cancelled/',
            metadata={
                'user_id': request.user.id
            }
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        messages.error(request, f"Something went wrong with the payment gateway. {str(e)}")
        return redirect('cart')


@login_required
def payment_successful(request):
    context = get_site_context()
    session_id = request.GET.get('session_id')
    
    if not session_id:
        messages.error(request, "Invalid request for payment success.")
        return redirect('home')

    try:
        session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = stripe.PaymentIntent.retrieve(session.payment_intent)
        
        # Check if order already exists
        if Order.objects.filter(stripe_payment_intent=payment_intent.id).exists():
            messages.info(request, "This order has already been processed.")
            return render(request, 'core/payment_successful.html', context)

        # Create Order
        order = Order.objects.create(
            user=request.user,
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            email=request.user.email,
            total_paid=session.amount_total / 100, # Convert from cents to dollars
            stripe_payment_intent=payment_intent.id,
            is_paid=True
        )

        # Get cart items and create OrderItems
        cart_items = Cart.objects.filter(user=request.user)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity,
                price=cart_item.item.price # Save price at time of purchase
            )

        # Clear the user's cart
        cart_items.delete()

        messages.success(request, "Payment Successful! Your order has been placed.")
        return render(request, 'core/payment_successful.html', context)

    except stripe.error.StripeError as e:
        messages.error(request, f"There was an error processing your payment: {str(e)}")
        return redirect('home')
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect('home')


def payment_cancelled(request):
    context = get_site_context()
    messages.error(request, "Your payment was cancelled. You have not been charged.")
    return render(request, 'core/payment_cancelled.html', context)