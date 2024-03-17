from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem, Inventory
from .forms import ProductForm, InventoryForm, OrderItemForm

# Views for Product model

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

# Views for Order model

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})


# Views for OrderItem model

def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'order_item_list.html', {'order_items': order_items})

def order_item_detail(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    return render(request, 'order_item_detail.html', {'order_item': order_item})

def add_order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_item_list')
    else:
        form = OrderItemForm()
    return render(request, 'add_order_item.html', {'form': form})

def edit_order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('order_item_list')
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, 'edit_order_item.html', {'form': form, 'order_item': order_item})

def delete_order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        order_item.delete()
        return redirect('order_item_list')
    return render(request, 'delete_order_item.html', {'order_item': order_item})

# Views for Inventory model

def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory_detail.html', {'inventory': inventory})

def restock_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'restock_inventory.html', {'form': form, 'inventory': inventory})

def low_stock_alert_list(request):
    low_stock_inventories = Inventory.objects.filter(low_stock_alert=True)
    return render(request, 'low_stock_alert_list.html', {'low_stock_inventories': low_stock_inventories})

def adjust_restock_level(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('low_stock_alert_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'adjust_restock_level.html', {'form': form, 'inventory': inventory})


def home(request):
    return render(request, 'store/index.html')