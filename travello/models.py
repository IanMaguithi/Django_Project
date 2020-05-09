from django.db import models


# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
