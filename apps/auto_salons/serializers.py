from rest_framework import serializers

from apps.auto_salons.models import AutoSalonModel
from apps.cars.serializers import CarSerializer


class AutoSalonSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoSalonModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
