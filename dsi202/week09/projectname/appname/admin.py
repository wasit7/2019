from django.contrib import admin
from .models import Customer, Car, Rent

class CarAdmin(admin.ModelAdmin):
    fields = ('brand', 'model', 'price')
admin.site.register(Car, CarAdmin)