from django.contrib import admin
from .models import (
    CustomUser, BaseConfig, HomeConfig, HomeImages, HomeLinks,
    AboutConfig, MenuConfig, MenuItems, OrderConfig, OrderItems,
    ContactConfig, Contact, WorkConfig, Workshop, ScheduleConfig,
    Booking, Cart
)

# Register all models here to make them accessible in the admin interface.

admin.site.register(CustomUser)
admin.site.register(BaseConfig)
admin.site.register(HomeConfig)
admin.site.register(HomeImages)
admin.site.register(HomeLinks)
admin.site.register(AboutConfig)
admin.site.register(MenuConfig)
admin.site.register(MenuItems)
admin.site.register(OrderConfig)
admin.site.register(OrderItems)
admin.site.register(ContactConfig)
admin.site.register(Contact)
admin.site.register(WorkConfig)
admin.site.register(Workshop)
admin.site.register(ScheduleConfig)
admin.site.register(Booking)
admin.site.register(Cart)