from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Item(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()