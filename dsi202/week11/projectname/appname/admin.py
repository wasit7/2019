from django.contrib import admin
from .models import Customer, Car, Rent

class CarAdmin(admin.ModelAdmin):
    fields = ('brand', 'model', 'price')
    list_display = ('id','brand', 'model', 'price')
    list_filter = ('model',)
    list_editable = ('brand', 'model', 'price')
admin.site.register(Car, CarAdmin)

class CustomerAdmin(admin.ModelAdmin):
    fields=('first_name', 'last_name', 'telephone', 'email')
    list_display = ('first_name', 'last_name', 'telephone', 'email')
admin.site.register(Customer, CustomerAdmin)

class RentAdmin(admin.ModelAdmin):
    fields = ('customer', 'car', 'cost')
    list_display = ('customer', 'car', 'cost')
admin.site.register(Rent, RentAdmin)