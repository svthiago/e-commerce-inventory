from django.db import models

# Create your models here.

class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ProductAmount = models.IntegerField()