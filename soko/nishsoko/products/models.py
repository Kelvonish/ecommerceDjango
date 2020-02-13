from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import reverse
# Create your models here.
class AddProduct (models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    updated=models.DateTimeField(auto_now=False, auto_now_add=False)
    image=models.ImageField( height_field=None, width_field=None, max_length=100)
    image2=models.ImageField( height_field=None, width_field=None, max_length=100)
    image3=models.ImageField( height_field=None, width_field=None, max_length=100)
    Clothes = 'Clothes'
    Shoes= 'Shoes'

    CATEGORY_CHOICES = [
        (Clothes, 'Clothes'),
        (Shoes, 'Shoes'),

    ]
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=Clothes,
    )

    def __str__(self):
        return self.title

