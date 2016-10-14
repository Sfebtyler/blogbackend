from django.db import models
from django import forms
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from decimal import Decimal


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



class Toppings(models.Model):
    topping = models.CharField(max_length=1000, default='')
    price = models.DecimalField(max_digits=50, decimal_places=1, default=0.00)

class Crusts(models.Model):
    crust = models.CharField(max_length=1000, default='')
    price = models.DecimalField(max_digits=50, decimal_places=1, default=0.00)

class PizzaSize(models.Model):
    size = models.CharField(max_length=1000, default='')
    price = models.DecimalField(max_digits=50, decimal_places=1, default=0.00)

class Order(models.Model):

    toppings = models.ManyToManyField(Toppings)
    crust = models.ForeignKey(Crusts, default='')
    size = models.ForeignKey(PizzaSize, default='')

    finalprice = models.DecimalField(max_digits=50, decimal_places=1, blank=True, null= True, default=0.00)
