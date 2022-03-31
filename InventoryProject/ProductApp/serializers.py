from rest_framework import serializers
from ProductApp.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=("ProductId", "ProductName", "ProductPrice", "ProductAmount")
