# In core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

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

class homeConfig(models.Model):
    image = models.ImageField(upload_to='homeconfig/', blank=True, null=True)
    def __str__(self):
        return f'Home Configuration {self.id}'

class home(models.Model):
    image = models.ImageField(upload_to='homeconfig2/', blank=True, null=True)
    instragram = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f'Home Configuration 2 {self.id}'
    

class AboutConfig(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "About Configuration"
    
class MenuConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title if self.title else "Menu Configuration"

class Menu(models.Model):
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Menu Item"
    
class ContactConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    site_email = models.EmailField(max_length=254, blank=True, null=True)
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


class OrderConfig(models.Model):
    image = models.ImageField(upload_to='order/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Order Configuration"

class Order(models.Model):
    schedule_choice = (
        (' Up to 30 minutes', 'Up to 30 minutes'),
        ('  Schedule for later', ' Schedule for later')
    )
    schedule_choices = models.CharField(max_length=50, choices=schedule_choice, default=' Up to 30 minutes')
    schedule_for_later_choice = (
        ('day', 'day'),
        ('time', 'time'),
    )
    schedule_for_later = models.CharField(max_length=50, choices=schedule_for_later_choice, default='day')
    day_choices = (
        ('today', 'today'),
        ('tommarow', 'tommarow'),
    )
    day = models.CharField(max_length=50, choices=day_choices, default='today')
    time_choices = (
        ('3.45am', '3.45am'),
        ('4.00am', '4.00am'),
        ('4.15am', '4.15am'),
        ('4.30am', '4.30am'),
        ('4.45am', '4.45am'),
        ('5.00am', '5.00am'),
        ('5.15am', '5.15am'),
        ('5.30am', '5.30am'),
        ('5.45am', '5.45am'),
        ('6.00am', '6.00am'),
        ('6.15am', '6.15am'),
        ('6.30am', '6.30am'),
        ('6.45am', '6.45am'),
        ('7.00am', '7.00am'),
        ('7.15am', '7.15am'),
        ('7.30am', '7.30am'),
        ('7.45am', '7.45am'),
        ('8.00am', '8.00am'),
        ('8.15am', '8.15am'),
        ('8.30am', '8.30am'),)
    time_choices = models.CharField(max_length=50, choices=time_choices, default='3.45am')
    pickup_location= models.CharField(max_length=100, blank=True, null=True)
    delivery_location = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f'Order {self.id} - {self.schedule_choice}'
    
class item(models.Model):
    image = models.ImageField(upload_to='item/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name if self.name else "Item"

class WorkConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title if self.title else "Work Configuration"
    
class Work(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Cost in dollars")
    def __str__(self):
        return self.Name if self.Name else "Work Item"

class ScheduleConfig(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    select_date = models.DateField(blank=True, null=True, help_text="Select a date for the schedule")
    select_time = models.TimeField(blank=True, null=True, help_text="Select a time for the schedule")

    def __str__(self):
        return self.title if self.title else "Schedule Configuration"

class FarmBooking(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else "Farm Booking Entry"
    class Meta:
        ordering = ['-id']

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user.username} - {self.item.name} ({self.quantity})'
    
    class Meta:
        unique_together = ('user', 'item')  # Prevents duplicate items in the cart for the same user
