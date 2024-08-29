from apps.cars.choices.body_type import BodyTypeChoices

from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    # year
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_range = filters.RangeFilter('year')
    year_in = filters.BaseInFilter(field_name='year', lookup_expr='in')
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    year_lte = filters.NumberFilter(field_name='year', lookup_expr='lte')
    year_gte = filters.NumberFilter(field_name='year', lookup_expr='gte')
    # brand
    brand_startswith = filters.CharFilter(field_name='brand', lookup_expr='startswith')
    brand_endswith = filters.CharFilter(field_name='brand', lookup_expr='endswith')
    # model
    model_startswith = filters.CharFilter(field_name='model', lookup_expr='startswith')
    model_endswith = filters.CharFilter(field_name='model', lookup_expr='endswith')
    # price
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_range = filters.RangeFilter(field_name='price', lookup_expr='range')
    price_in = filters.BaseInFilter(field_name='price', lookup_expr='in')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    # color
    color = filters.CharFilter(field_name='color', lookup_expr='exact')
    # state
    state = filters.CharFilter(field_name='state', lookup_expr='exact')
    state_in = filters.BaseInFilter(field_name='state', lookup_expr='in')

    body = filters.ChoiceFilter(field_name='body_type', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'brand',
            'price',
            'year',
            'state',
            'color',
            'model',
            'body_type'
        ))
