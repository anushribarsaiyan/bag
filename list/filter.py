import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):


    class Meta:
        model =Grocery_Bag
        fields = '__all__'
        exclude = ['item_name','item_quantity','item_status']
