from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'color',
                  'region', 'price', 'body_type', 'photo',
                  'currency', 'transmission', 'engine', 'created_at', 'updated_at')


class CarFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}
