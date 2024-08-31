from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel
from core.services.file_services import FileService

from apps.auto_salons.models import AutoSalonModel
from apps.cars.choices import BodyTypeChoices, CurrencyType, EngineType, TransmissionType
from apps.cars.managers import CarManager, CarQuerySet


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    brand = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    model = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    year = models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)))
    color = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    price = models.IntegerField(validators=(V.MinValueValidator(100), V.MaxValueValidator(1_000_000_000)))
    region = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    body_type = models.CharField(max_length=21, choices=BodyTypeChoices.choices)
    currency = models.CharField(max_length=3, choices=CurrencyType.choices, default='USD')
    engine = models.CharField(max_length=25,choices=EngineType.choices)
    transmission = models.CharField(max_length=24, choices=TransmissionType.choices)
    auto_salon = models.ForeignKey(AutoSalonModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='cars')
    photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True)

    objects = CarManager
