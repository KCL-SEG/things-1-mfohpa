from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=520)
    quantity = models.IntegerField()