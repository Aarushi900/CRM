import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='date_created', lookup_expr='gte')
    end_date_date = django_filters.DateFilter(
        field_name='date_created', lookup_expr='lte')
    category_name = django_filters.CharFilter(
        field_name='product__category', lookup_expr='icontains', label='Category Name')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = {'customer', 'date_created'}
