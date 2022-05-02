from django.db import models


# Create your models here.
class Relatives(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()
    family_relationship = models.CharField(max_length=255, default='Familiar')
