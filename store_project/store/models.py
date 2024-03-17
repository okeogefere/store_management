from django.db import models
from shortuuid.django_fields import ShortUUIDField
from users.models import User

# Create your models here.
PRODUCT_TYPE = (
    ('laptop', 'Laptop'),
    ('desktop', 'Desktop'),
    ('phones', 'Phones'),
    ('other', 'Other'),
)
BRAND = (
    ('hp', 'Hp'),
    ('acer', 'Acer'),
    ('apple', 'Apple'),
    ('dell', 'Dell'),
    ('asus', 'Asus'),
    ('samsung', 'Samsung'),
    ('infinix', 'Infinix'),
    ('lg', 'Lg'),
    ('sony', 'Sony'),
    ('other', 'Other'),

)
CATEGORY = (
        ('computers', 'Computers'),
        ('mobile Phones', 'Mobile Phones'),
        ('other', 'Other'),

)
STATUS =(('processing', 'Processing'), 
        ('shipped', 'Shipped'), 
        ('delivered', 'Delivered')
        )

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=100, default='other')
    brand = models.CharField(max_length=100, choices=BRAND, default='other')
    category = models.CharField(max_length=100, choices=CATEGORY, default='Other')

    # pid = ShortUUIDField(length=5, max_length=40, prefix="PID-", alphabet="abcdefghijklmnop1234567890", primary_key=True,)
    sku = ShortUUIDField(length=5, max_length=10, prefix="SKU-", alphabet="ABCDEFG1234567890", unique=True)

    quantity = models.IntegerField()
    available_qty = models.IntegerField()

    production_date = models.DateField()
    addded_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def is_available(self):
        return self.quantity > 0

    def reduce_quantity(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()

    def increase_quantity(self, quantity):
        self.quantity += quantity
        self.save()


    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    address = models.TextField()
    email = models.EmailField()

    phone_number = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=200, choices=STATUS, default='other')
    order_date = models.DateTimeField(auto_now_add=True)
    # order_id = ShortUUIDField(length=5, max_length=10, prefix="OID-", alphabet="abcdefghijklmnop1234567890", unique=True)

    
    def calculate_total_price(self):
        total = sum(item.subtotal for item in self.orderitem_set.all())
        self.total_price = total
        self.save()

    def update_status(self, new_status):
        self.status = new_status
        self.save()

    def generate_summary(self):
        summary = f"Order Summary for {self.customer_name}\n"
        for item in self.orderitem_set.all():
            summary += f"{item.product.name}: {item.quantity} x ${item.unit_price} = ${item.subtotal}\n"
        summary += f"Total Price: ${self.total_price}\n"
        return summary

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        self.subtotal = self.unit_price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    restock_level = models.IntegerField()
    low_stock_alert = models.BooleanField(default=False)
    last_restock_date = models.DateField()

    def is_low_stock(self):
        return self.product.quantity < self.restock_level

    def restock(self, quantity):
        self.product.quantity += quantity
        self.product.save()

    def check_low_stock_alert(self):
        if self.is_low_stock():
            self.low_stock_alert = True
            self.save()

    def __str__(self):
        return f"Inventory for {self.product.name}"