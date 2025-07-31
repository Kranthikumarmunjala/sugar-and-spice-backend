# # In core/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from ckeditor.fields import RichTextField



# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True, blank=False, null=False)

#     def __str__(self):
#         return self.username

# class TitleConfig(models.Model):
#     logo = models.ImageField(upload_to='home/', blank=True, null=True)
#     logo_title = models.CharField(max_length=100, blank=True, null=True)
#     logo_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     instragram = models.URLField(max_length=200, blank=True, null=True)
#     facebook = models.URLField(max_length=200, blank=True, null=True)
#     about_title = models.CharField(max_length=100, blank=True, null=True)
#     about_description = models.TextField(blank=True, null=True)  
#     about_image = models.ImageField(upload_to='about/', blank=True, null=True)
#     menu_title = models.CharField(max_length=100, blank=True, null=True)
#     menu_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     order_online_title = models.CharField(max_length=100, blank=True, null=True)
#     order_online_description = models.TextField(blank=True, null=True)
#     order_online_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     oredr_online_image = models.ImageField(upload_to='order/', blank=True, null=True)
#     contact_title = models.CharField(max_length=100, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     contact_site_email = models.EmailField(max_length=254, blank=True, null=True)
#     contact_phone = models.CharField(max_length=15, blank=True, null=True)
#     contact_text = models.TextField(blank=True, null=True)
#     contact_image = models.ImageField(upload_to='contact/', blank=True, null=True)
#     contact_map_url = models.URLField(max_length=200, blank=True, null=True)
#     workshop_title = models.CharField(max_length=100, blank=True, null=True)
#     schedule_title = models.CharField(max_length=100, blank=True, null=True)
#     schedule_description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.logo_title if self.logo_title else "Title Configuration"


# class HomePageImage(models.Model):
#     image = models.ImageField(upload_to='home/', blank=True, null=True)

#     def __str__(self):
#         return self.image.name if self.image else f"Image ID: {self.id}"

# class MenuItems(models.Model):
#     image = models.ImageField(upload_to='menu/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

#     def __str__(self):
#         return self.name if self.name else "Menu Item"
    
# class OrderItems(models.Model):
#     image = models.ImageField(upload_to='item/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#     def __str__(self):
#         return self.name if self.name else "Order Item"
    
    
# class Contact(models.Model):
#    first_name = models.CharField(max_length=100, blank=True, null=True)
#    last_name = models.CharField(max_length=100, blank=True, null=True)
#    email = models.EmailField(max_length=254, blank=True, null=True)
#    phone = models.CharField(max_length=15, blank=True, null=True)
#    message = models.TextField(blank=True, null=True)
#    created_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Contact Entry"
   
#    class Meta:
#        ordering = ['-created_at']

    
# class Workshop(models.Model):
#     image = models.ImageField(upload_to='workshop/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     duration = models.CharField(max_length=100, blank=True, null=True)
#     cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Cost in dollars")

#     def __str__(self):
#         return self.name if self.name else "Workshop Item"
    

# class Booking(models.Model):
#     workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='bookings', null=True)
#     booking_date = models.DateField(null=True, blank=True)
#     booking_time = models.TimeField(null=True, blank=True)
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f'Booking for {self.workshop.name} on {self.booking_date} at {self.booking_time}'
    
#     class Meta:
#         # Prevent the same time slot for the same workshop from being booked twice
#         unique_together = ('workshop', 'booking_date', 'booking_time')
#         ordering = ['booking_date', 'booking_time']


# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items')
#     item = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.item.name} ({self.quantity})'
    
#     class Meta:
#         unique_together = ('user', 'item')  # Prevents duplicate items in the cart for the same user




# In core/models.py

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from ckeditor.fields import RichTextField



# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True, blank=False, null=False)

#     def __str__(self):
#         return self.username

# class TitleConfig(models.Model):
#     logo = models.ImageField(upload_to='home/', blank=True, null=True)
#     logo_title = models.CharField(max_length=100, blank=True, null=True)
#     logo_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     instragram = models.URLField(max_length=200, blank=True, null=True)
#     facebook = models.URLField(max_length=200, blank=True, null=True)
#     about_title = models.CharField(max_length=100, blank=True, null=True)
#     about_description = models.TextField(blank=True, null=True)  
#     about_image = models.ImageField(upload_to='about/', blank=True, null=True)
#     menu_title = models.CharField(max_length=100, blank=True, null=True)
#     menu_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     order_online_title = models.CharField(max_length=100, blank=True, null=True)
#     order_online_description = models.TextField(blank=True, null=True)
#     order_online_subtitle = models.CharField(max_length=200, blank=True, null=True)
#     oredr_online_image = models.ImageField(upload_to='order/', blank=True, null=True)
#     contact_title = models.CharField(max_length=100, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     contact_site_email = models.EmailField(max_length=254, blank=True, null=True)
#     contact_phone = models.CharField(max_length=15, blank=True, null=True)
#     contact_text = models.TextField(blank=True, null=True)
#     contact_image = models.ImageField(upload_to='contact/', blank=True, null=True)
#     contact_map_url = models.URLField(max_length=200, blank=True, null=True)
#     workshop_title = models.CharField(max_length=100, blank=True, null=True)
#     schedule_title = models.CharField(max_length=100, blank=True, null=True)
#     schedule_description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.logo_title if self.logo_title else "Title Configuration"


# class HomePageImage(models.Model):
#     image = models.ImageField(upload_to='home/', blank=True, null=True)

#     def __str__(self):
#         return self.image.name if self.image else f"Image ID: {self.id}"

# class MenuItems(models.Model):
#     image = models.ImageField(upload_to='menu/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

#     def __str__(self):
#         return self.name if self.name else "Menu Item"
    
# class OrderItems(models.Model):
#     image = models.ImageField(upload_to='item/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#     def __str__(self):
#         return self.name if self.name else "Order Item"
    
    
# class Contact(models.Model):
#    first_name = models.CharField(max_length=100, blank=True, null=True)
#    last_name = models.CharField(max_length=100, blank=True, null=True)
#    email = models.EmailField(max_length=254, blank=True, null=True)
#    phone = models.CharField(max_length=15, blank=True, null=True)
#    message = models.TextField(blank=True, null=True)
#    created_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Contact Entry"
   
#    class Meta:
#        ordering = ['-created_at']

    
# class Workshop(models.Model):
#     image = models.ImageField(upload_to='workshop/', blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     duration = models.CharField(max_length=100, blank=True, null=True)
#     cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Cost in dollars")

#     def __str__(self):
#         return self.name if self.name else "Workshop Item"
    

# class Booking(models.Model):
#     workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='bookings', blank=True, null=True)
#     booking_date = models.DateField(null=True, blank=True)
#     booking_time = models.TimeField(null=True, blank=True)
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)

#     def __str__(self):
#         if self.workshop:
#             return f'Booking for {self.workshop.name} on {self.booking_date} at {self.booking_time}'
#         else:
#             return f'Booking by {self.first_name} {self.last_name} on {self.booking_date} (No Workshop Assigned)' # <-- ADDED ' HERE
    
#     class Meta:
#         # Prevent the same time slot for the same workshop from being booked twice
#         unique_together = ('workshop', 'booking_date', 'booking_time')
#         ordering = ['booking_date', 'booking_time']


# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items',blank=True, null=True)
#     item = models.ForeignKey(OrderItems, on_delete=models.CASCADE,blank=True, null=True)
#     quantity = models.PositiveIntegerField(default=1,blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.item.name} ({self.quantity})'
    
#     class Meta:
#         unique_together = ('user', 'item')  # Prevents duplicate items in the cart for the same user


# # --- NEW MODELS FOR PAID ORDERS ---

# class Order(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
#     first_name = models.CharField(max_length=100,blank=True, null=True)
#     last_name = models.CharField(max_length=100,blank=True, null=True)
#     email = models.EmailField()
#     total_paid = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
#     stripe_payment_intent = models.CharField(max_length=255,blank=True, null=True)
#     is_paid = models.BooleanField(default=False,blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"Order {self.id} - {self.first_name} {self.last_name}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,blank=True, null=True)
#     item = models.ForeignKey(OrderItems, on_delete=models.CASCADE, related_name='order_items',blank=True, null=True)
#     quantity = models.PositiveIntegerField(default=1,blank=True, null=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True) # Price at the time of purchase

#     def __str__(self):
#         return f"{self.quantity} x {self.item.name} for Order {self.order.id}"












from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.username

class TitleConfig(models.Model):
    logo = models.ImageField(upload_to='home/', blank=True, null=True)
    logo_title = models.CharField(max_length=100, blank=True, null=True)
    logo_subtitle = models.CharField(max_length=200, blank=True, null=True)
    instragram = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    about_title = models.CharField(max_length=100, blank=True, null=True)
    about_description = models.TextField(blank=True, null=True)  
    about_image = models.ImageField(upload_to='about/', blank=True, null=True)
    menu_title = models.CharField(max_length=100, blank=True, null=True)
    menu_subtitle = models.CharField(max_length=200, blank=True, null=True)
    order_online_title = models.CharField(max_length=100, blank=True, null=True)
    order_online_description = models.TextField(blank=True, null=True)
    order_online_subtitle = models.CharField(max_length=200, blank=True, null=True)
    oredr_online_image = models.ImageField(upload_to='order/', blank=True, null=True)
    contact_title = models.CharField(max_length=100, blank=True, null=True)
    contact_address = models.CharField(max_length=255, blank=True, null=True)
    contact_site_email = models.EmailField(max_length=254, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_text = models.TextField(blank=True, null=True)
    contact_image = models.ImageField(upload_to='contact/', blank=True, null=True)
    contact_map_url = models.URLField(max_length=200, blank=True, null=True)
    workshop_title = models.CharField(max_length=100, blank=True, null=True)
    schedule_title = models.CharField(max_length=100, blank=True, null=True)
    schedule_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.logo_title if self.logo_title else "Title Configuration"


class HomePageImage(models.Model):
    image = models.ImageField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.image.name if self.image else f"Image ID: {self.id}"

class MenuItems(models.Model):
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Menu Item"
    
class OrderItems(models.Model):
    image = models.ImageField(upload_to='item/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name if self.name else "Order Item"
    
    
class Contact(models.Model):
   first_name = models.CharField(max_length=100, blank=True, null=True)
   last_name = models.CharField(max_length=100, blank=True, null=True)
   email = models.EmailField(max_length=254, blank=True, null=True)
   phone = models.CharField(max_length=15, blank=True, null=True)
   message = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Contact Entry"
   
   class Meta:
       ordering = ['-created_at']

    
class Workshop(models.Model):
    image = models.ImageField(upload_to='workshop/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Cost in dollars")

    def __str__(self):
        return self.name if self.name else "Workshop Item"
    

class Booking(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='bookings', blank=True, null=True)
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.workshop:
            return f'Booking for {self.workshop.name} on {self.booking_date} at {self.booking_time}'
        else:
            return f'Booking by {self.first_name} {self.last_name} on {self.booking_date} (No Workshop Assigned)' # <-- ADDED ' HERE
    
    class Meta:
        # Prevent the same time slot for the same workshop from being booked twice
        unique_together = ('workshop', 'booking_date', 'booking_time')
        ordering = ['booking_date', 'booking_time']


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items',blank=True, null=True)
    item = models.ForeignKey(OrderItems, on_delete=models.CASCADE,blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1,blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.item.name} ({self.quantity})'
    
    class Meta:
        unique_together = ('user', 'item')  # Prevents duplicate items in the cart for the same user


# --- NEW MODELS FOR PAID ORDERS ---

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField()
    total_paid = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    stripe_payment_intent = models.CharField(max_length=255,blank=True, null=True)
    is_paid = models.BooleanField(default=False,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,blank=True, null=True)
    item = models.ForeignKey(OrderItems, on_delete=models.CASCADE, related_name='order_items',blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1,blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True) # Price at the time of purchase

    def __str__(self):
        return f"{self.quantity} x {self.item.name} for Order {self.order.id}"