from django.contrib import admin

from .models import Menu, Category, Reservation


admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Reservation)
