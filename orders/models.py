# from django.db.models import (
#     Model,
#     IntegerField,
#     DecimalField,
#     CharField,
#     SET_NULL,
#     ForeignKey,
#     OneToOneField,
#     DateTimeField,
#     BooleanField,
#     CASCADE,
# )

# # Create your models here.

# from users.models import User
# from products.models import Product


# class Order(Model):
#     user = ForeignKey(User, on_delete=SET_NULL, null=True)
#     total_price = CharField(max_length=250, blank=True)
#     is_delivered = BooleanField(default=False)
#     delivered_at = DateTimeField(auto_now_add=False, null=True, blank=True)
#     created_at = DateTimeField(auto_now_add=True)


# class OrderItem(Model):
#     product = ForeignKey(Product, on_delete=SET_NULL, null=True)
#     order = ForeignKey(Order, on_delete=SET_NULL, null=True)
#     quantity = IntegerField(null=True, blank=True, default=0)
#     price = CharField(max_length=250, blank=True)


# class ShippingAddress(Model):
#     order = OneToOneField(Order, on_delete=CASCADE, null=True, blank=True)
#     address = CharField(max_length=250, blank=True)
#     city = CharField(max_length=100, blank=True)
#     postal_code = CharField(max_length=100, blank=True)
