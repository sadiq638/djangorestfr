from django.db import models

# Create your models here.
class Obj(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
     