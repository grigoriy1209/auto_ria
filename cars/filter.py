from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for key, value in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case _:
                raise ValidationError(f'Invalid value for {key}')
    return qs
