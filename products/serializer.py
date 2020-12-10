from rest_framework.serializers import ModelSerializer
from .models import ProductModel


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['user']
