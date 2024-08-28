from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from cars.models import CarModel
from cars.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    available_filters = {
        'price_gt', 'price_lt', 'price_lte', 'price_gte',
        'year_lte', 'year_gte', 'year_gt', 'year',
        'brand_start', 'brand_contains', 'brand_end',
        'model', 'color', 'state', 'create_at', 'order'
    }

    for key, value in query.items():
        match key:
            # price
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_lte':
                qs = qs.filter(price__lte=value)
            case 'price_gte':
                qs = qs.filter(price__gte=value)
            # year
            case 'year_lte':
                qs = qs.filter(year__lte=value)
            case 'year_gte':
                qs = qs.filter(year__gte=value)
            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'year':
                qs = qs.filter(year=value)
            # brand
            case 'brand_start':
                qs = qs.filter(brand__istartswith=value)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=value)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=value)
            # model
            case 'model':
                qs = qs.filter(model=value)
            # color
            case 'color':
                qs = qs.filter(color=value)
            # state
            case 'state':
                qs = qs.filter(state=value)
                # create_car
            case 'create_at':
                qs = qs.filter(create_at__year=value)

            case 'order':
                fields = list(CarSerializer.Meta.fields)
                fields.extend([[f'-{field}' for field in fields]])

                if value not in fields:
                    raise ValidationError({"details": f'Please choice order from {", ".join(fields)}'})

                qs = qs.order_by(value)

            case _:
                raise ValidationError(f'Filter {key} not supported.Available filters are: {", ".join(available_filters)}')
    return qs
