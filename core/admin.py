
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(CustomUser, UserAdmin)
admin.site.register(BaseConfig)
admin.site.register(homeConfig)
admin.site.register(home)
admin.site.register(AboutConfig)
admin.site.register(MenuConfig)
admin.site.register(Menu)
admin.site.register(ContactConfig)
admin.site.register(Contact)
admin.site.register(OrderConfig)
admin.site.register(Order)
admin.site.register(item)
admin.site.register(WorkConfig)
admin.site.register(Work)
admin.site.register(ScheduleConfig)
admin.site.register(FarmBooking)
admin.site.register(Cart)

