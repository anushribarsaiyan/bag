from django.forms import ModelForm

from list.models import Grocery_Bag


class Grocery_BagForm(ModelForm):
    class Meta:
        model = Grocery_Bag
        fields = '__all__'