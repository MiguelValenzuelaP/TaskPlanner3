# from django.db.models import (
#     Model,
#     IntegerField,
#     DecimalField,
#     CharField,
#     DateTimeField,
#     ImageField,
#     SlugField,
#     ForeignKey,
#     SET_NULL,
# )
# from users.models import User


# # Create your models here.
# class Product(Model):
#     slug = SlugField(max_length=50, null=True, blank=True)
#     user = ForeignKey(User)
#     name = CharField(max_length=100, null=True, blank=True)
#     image = ImageField(default="placeholder.png")
#     category = CharField(max_length=100, blank=True)
#     description = CharField(max_leng=100, blank=True)
#     rating = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     num_reviews = IntegerField(default=0)
#     price = DecimalField(max_digits=10, max_places=2, null=True, blank=True)
#     count_in_stock = IntegerField(default=0)
#     created = DateTimeField(auto_now_add=True)


# class Review(Model):
#     product = ForeignKey(Product, on_delete=SET_NULL, null=True)
#     user = ForeignKey(User, on_delete=SET_NULL, null=True)
#     rating = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     description = CharField(max_length=100, blank=True)
#     created = DateTimeField(auto_now_add=True)
