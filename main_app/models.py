from django.db import models

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'description: {self.description}, quantity: {self.quantity}'
