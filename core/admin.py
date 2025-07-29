# # In core/admin.py

# from django.contrib import admin
# from .models import (
#     CustomUser, TitleConfig, HomePageImage, MenuItems, 
#     OrderItems, Contact, Workshop, Booking, Cart
# )

# # Register all models here to make them accessible in the admin interface.

# admin.site.register(CustomUser)
# admin.site.register(TitleConfig) # The new, consolidated config model
# admin.site.register(HomePageImage)
# admin.site.register(MenuItems)
# admin.site.register(OrderItems)
# admin.site.register(Contact)
# admin.site.register(Workshop)
# admin.site.register(Booking)
# admin.site.register(Cart)



# In core/admin.py
from django.contrib import admin
from .models import (
    CustomUser, TitleConfig, HomePageImage, MenuItems, 
    OrderItems, Contact, Workshop, Booking, Cart,
    Order, OrderItem  # <-- Import new models
)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['item'] # Use a search box for items instead of a dropdown
    extra = 0 # Don't show extra empty forms

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'total_paid', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'user__username')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'stripe_payment_intent')

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TitleConfig)
admin.site.register(HomePageImage)
admin.site.register(MenuItems)
admin.site.register(OrderItems)
admin.site.register(Contact)
admin.site.register(Workshop)
admin.site.register(Booking)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin) # <-- Register new Order model with custom admin
admin.site.register(OrderItem) # <-- Register new OrderItem model