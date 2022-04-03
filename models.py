from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    vat = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category)

