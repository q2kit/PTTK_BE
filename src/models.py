from django.db import models
import uuid


class Account(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


class Customer(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


class Seller(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)
    shop_name = models.CharField(max_length=100)
    shop_description = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
