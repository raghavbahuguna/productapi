from django.db import models

# Create your models here.
class Product(models.Model):
    productid=models.IntegerField()
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name