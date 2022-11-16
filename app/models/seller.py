from django.db import models
from account import Account

class Seller(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    shop_name = models.CharField(max_length=100)
    shop_description = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
