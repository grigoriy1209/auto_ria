from django.db import models


class EngineType(models.TextChoices):
    gasoline = 'Gasoline',
    gas = 'Gas',
    diesel = 'Diesel',
    electricity = 'Electricity',
    hybrid = 'Hybrid',

