from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    # URLs for Product views
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),

    # URLs for Order views
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),

    # URLs for OrderItem views
    path('order_items/', views.order_item_list, name='order_item_list'),
    path('order_items/<int:pk>/', views.order_item_detail, name='order_item_detail'),
    path('order_items/add/', views.add_order_item, name='add_order_item'),
    path('order_items/<int:pk>/edit/', views.edit_order_item, name='edit_order_item'),
    path('order_items/<int:pk>/delete/', views.delete_order_item, name='delete_order_item'),

    # URLs for Inventory views
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/<int:pk>/restock/', views.restock_inventory, name='restock_inventory'),

    # URLs for managing low stock alerts
    path('low_stock_alert/', views.low_stock_alert_list, name='low_stock_alert_list'),
    path('low_stock_alert/<int:pk>/adjust_restock_level/', views.adjust_restock_level, name='adjust_restock_level'),
]