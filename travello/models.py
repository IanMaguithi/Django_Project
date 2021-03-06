from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
