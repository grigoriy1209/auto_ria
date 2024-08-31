from django.db import models


class CurrencyType(models.TextChoices):
    USD = 'USD',
    EUR = 'EUR',
    UAH = 'UAH',

