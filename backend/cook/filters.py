from django_filters import rest_framework as filters
from .models import Cook


class CookFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains', label='요리의 name')
    cook_ingredient = filters.CharFilter(field_name="cook_ingredient__name", lookup_expr='icontains', label='재료의 name')

    class Meta:
        model = Cook
        fields = [
            'name',
            'cook_ingredient',
        ]
