from django.db import models
from django.urls import reverse
#Used to generate URLs by reversing the URL patterns
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a type of product (e.g Food)')
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_description = models.TextField(max_length=1000, help_text='Enter a brief description of the product')

    product_category = models.ForeignKey(Category, help_text='Select the type of product for this item', on_delete=models.RESTRICT)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


"""
class Pair_Recommendation(models.Model):
    pair1 = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    pair2 = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f'{self.pair1} and {self.pair2}'

    def get_absolute_url(self):
        return reverse('pair_detail', args=[str(self.id)])
"""

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=4)
    security_code = models.CharField(max_length=3)
    payment_method = models.CharField(max_length=20)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])