from rest_framework import serializers
from .models import Product, Services, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'