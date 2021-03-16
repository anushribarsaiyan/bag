from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Grocery_Bag(models.Model):
    objects = None
    STATUS = (
        ('pending', 'Bought'),
        ('Not AVAILABLE', 'Not AVAILABLE'),
        ('PENDING', 'PENDING')

    )

    item_name = models.CharField(max_length=12)
    item_quantity = models.IntegerField()
    item_status = models.CharField(max_length=200, null=True, choices=STATUS)
    Date= models.DateTimeField()





