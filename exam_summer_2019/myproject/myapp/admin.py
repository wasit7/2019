from django.contrib import admin
from myapp.models import Customer,  Transaction, Item, Record

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]
admin.site.register(Customer, CustomerAdmin)

class TransactionAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Transaction._meta.fields]
admin.site.register(Transaction, TransactionAdmin)

class ItemAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Item._meta.fields]
admin.site.register(Item, ItemAdmin)

class RecordAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Record._meta.fields]
admin.site.register(Record, RecordAdmin)