from rest_framework.serializers import ModelSerializer
from .models import ProductModel, ProductImage


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['user']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
