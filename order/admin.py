from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.
class OrderItemList(admin.TabularInline):
	model = OrderItem
	extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'totalbook', 'created', 'updated', 'paid']
    list_filter = ['paid']
    exclude = ['name', 'email', 'phone']
    inlines = [OrderItemList]
    class Meta:
	    Model = Order
admin.site.register(Order, OrderAdmin)