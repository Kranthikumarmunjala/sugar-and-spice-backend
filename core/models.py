# In core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.username

class BaseConfig(models.Model):
    logo = models.ImageField(upload_to='home/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Base Configuration"
    
class HomeConfig(models.Model):
    image = models.ImageField(upload_to='homeconfig/', blank=True, null=True)

    def __str__(self):
        return f'Home Configuration {self.id}'
    
class HomeImages(models.Model):
    image = models.ImageField(upload_to='homeconfig2/', blank=True, null=True)

    def __str__(self):
        return f'Home Configuration 2 {self.id}'
    
class HomeLinks(models.Model):
    instagram = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Home Links {self.id}'
    
class AboutConfig(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True) # CHANGED FROM RichTextField

    def __str__(self):
        return self.title if self.title else "About Configuration"
    
class MenuConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Menu Configuration"
    
class MenuItems(models.Model):
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Menu Item"


class OrderConfig(models.Model):
    image = models.ImageField(upload_to='order/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Order Configuration"
    
class OrderItems(models.Model):
    image = models.ImageField(upload_to='item/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name if self.name else "Order Item"
    
# class ContactConfig(models.Model):
#     title = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     site_email = models.EmailField(max_length=254, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     text = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='contact/', blank=True, null=True)
#     map_url = models.URLField(max_length=200, blank=True, null=True)
#     def __str__(self):
#         return self.title if self.title else "Contact Configuration"
    
# class Contact(models.Model):
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Contact Entry"
    
#     class Meta:
#         ordering = ['-created_at']




class ContactConfig(models.Model):
   title = models.CharField(max_length=100, blank=True, null=True)
   address = models.CharField(max_length=255, blank=True, null=True)
   site_email = models.EmailField(max_length=254, blank=True, null=True)
   phone = models.CharField(max_length=15, blank=True, null=True)
   text = models.TextField(blank=True, null=True)
   image = models.ImageField(upload_to='contact/', blank=True, null=True)
   map_url = models.URLField(max_length=200, blank=True, null=True)
   
   def __str__(self):
       return self.title if self.title else "Contact Configuration"
    
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


class WorkConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Work Configuration"
    
class Workshop(models.Model):
    image = models.ImageField(upload_to='workshop/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Cost in dollars")

    def __str__(self):
        return self.name if self.name else "Workshop Item"
    
class ScheduleConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title if self.title else "Schedule Configuration"


# class Booking(models.Model):
#     first_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Booking Entry"
    
#     class Meta:
#         ordering = ['-id']  # Orders by the most recent booking first

class Booking(models.Model):
# Link the booking to a specific workshop
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='bookings', null=True)
    
    # Store the exact date and time of the booking
    booking_date = models.DateField()
    booking_time = models.TimeField()

    # User who made the booking
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Booking for {self.workshop.name} on {self.booking_date} at {self.booking_time}'
    
    class Meta:
        # Prevent the same time slot for the same workshop from being booked twice
        unique_together = ('workshop', 'booking_date', 'booking_time')
        ordering = ['booking_date', 'booking_time']





class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.item.name} ({self.quantity})'
    
    class Meta:
        unique_together = ('user', 'item')  # Prevents duplicate items in the cart for the same user




