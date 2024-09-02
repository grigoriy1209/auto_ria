from rest_framework import serializers

from apps.cars.models import CarModel, CarPhotoModel


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


class CarSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, required=False)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'color',
                  'region', 'price', 'body_type', 'currency',
                  'engine', 'transmission', 'auto_salon', 'photos', 'created_at', 'updated_at')

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        car = super().create(**validated_data)

        for photo_data in photos_data:
            CarPhotoModel.objects.create(car=car, **photo_data)
        return car

