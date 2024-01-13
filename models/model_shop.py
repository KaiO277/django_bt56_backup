from django.db import models

# Create your models here.

class product(models.Model):

    class Meta:
        app_label = 'shop'

    name = models.TextField(max_length=250)
    price = models.IntegerField()
    image = models.TextField()
    test = models.IntegerField()

    def __str__(self):
        return self.name