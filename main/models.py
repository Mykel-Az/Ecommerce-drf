from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    sub_category = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True)


    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products_brand')
    category = TreeForeignKey("Category", on_delete=models.SET_NULL, related_name='products_category', null=True, blank=True)
    is_digital  = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name