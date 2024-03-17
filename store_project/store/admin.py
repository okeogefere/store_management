from django.contrib import admin
from .models import *
# Register your models here.

class ProdctAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'brand', 'category', 'sku', 'quantity', 'added_by']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'user', 'product', 'quantity', 'total_price', 'order_date',]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price', 'subtotal']


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'restock_level', 'low_stock_alert', 'last_restock_date']

admin.site.register(Product, ProdctAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Inventory, InventoryAdmin)