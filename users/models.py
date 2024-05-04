# from django.db.models import (
#     Model,
#     CharField,
#     IntegerField,
#     ImageField,
#     DateTimeField,
#     BooleanField,
# )
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     PermissionsMixin,
#     UserManager,
# )
# from django.utils import timezone


# #TODO REFACTORIZAR LOS METODOS DE CREATEUSER AND SUPERUSER, PARA QUE QUEDE EN UN SOLO METODO
# #TODO REFACTORIZAR EL TYPING DE LAS VARIABLES
# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("discard email")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         return self._create_user(email, password, **extra_fields)


# # Create your models here.
# class User(Model, PermissionsMixin):
#     email = CharField(max_length=100, unique=True)
#     name = CharField(max_length=100)
#     last_name = CharField(max_length=100)
#     avatar = ImageField(default="avatar.png")
#     data_joined = DateTimeField(default=timezone.now)
#     is_staff = BooleanField(default=False)
#     objects = CustomUserManager()
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     class META:
#         ordering = ["-date_joined"]
