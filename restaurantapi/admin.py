from django.contrib import admin
from restaurantapi.models import Menu, MenuItem, Order

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',  'available']

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'cost', 'available', 'menu']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'MenuItem', 'time', 'operator','paid']

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)