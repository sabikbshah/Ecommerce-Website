from django.db import models
from products.models import *
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} - {self.products.name}"



class Order(models.Model):
    PAYMENT = (
        ('CASH','CASH'),
        ('CARD','CARD'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits = 10, decimal_places= 2)
    phone_no = models.CharField(max_length= 14, validators=[MinLengthValidator(10),MaxLengthValidator(14)])
    address = models.CharField(max_length = 100)
    payment_method = models.CharField(max_length = 50, choices =PAYMENT)
    payment_status = models.BooleanField(default=False,null = True)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
