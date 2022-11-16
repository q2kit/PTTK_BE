from django.db import models
from account import Account

class Customer(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.BooleanField(default=True)