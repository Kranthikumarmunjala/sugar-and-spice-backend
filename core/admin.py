# from django.contrib import admin
# from .models import (
#     CustomUser, BaseConfig,HomePageImage, HomeLinks,
#     AboutConfig, MenuConfig, MenuItems, OrderConfig, OrderItems,
#     ContactConfig, Contact, WorkConfig, Workshop, ScheduleConfig,
#     Booking, Cart
# )

# # Register all models here to make them accessible in the admin interface.

# admin.site.register(CustomUser)
# admin.site.register(BaseConfig)
# admin.site.register(HomePageImage)
# admin.site.register(HomeLinks)
# admin.site.register(AboutConfig)
# admin.site.register(MenuConfig)
# admin.site.register(MenuItems)
# admin.site.register(OrderConfig)
# admin.site.register(OrderItems)
# admin.site.register(ContactConfig)
# admin.site.register(Contact)
# admin.site.register(WorkConfig)
# admin.site.register(Workshop)
# admin.site.register(ScheduleConfig)
# admin.site.register(Booking)
# admin.site.register(Cart)


# In core/admin.py

from django.contrib import admin
from .models import (
    CustomUser, TitleConfig, HomePageImage, MenuItems, 
    OrderItems, Contact, Workshop, Booking, Cart
)

# Register all models here to make them accessible in the admin interface.

admin.site.register(CustomUser)
admin.site.register(TitleConfig) # The new, consolidated config model
admin.site.register(HomePageImage)
admin.site.register(MenuItems)
admin.site.register(OrderItems)
admin.site.register(Contact)
admin.site.register(Workshop)
admin.site.register(Booking)
admin.site.register(Cart)