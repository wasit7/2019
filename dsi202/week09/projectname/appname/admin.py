from django.contrib import admin
from .models import Customer, Car, Rent

class CarAdmin(admin.ModelAdmin):
    fields = ('brand', 'model', 'price')
    list_display = ('id','brand', 'model', 'price')
    list_filter = ('model',)
    list_editable = ('brand', 'model', 'price')
admin.site.register(Car, CarAdmin)