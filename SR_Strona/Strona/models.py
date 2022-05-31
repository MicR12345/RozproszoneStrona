from django.db import models

# Create your models here.

class Data(models.Model):
    money = models.IntegerField()
    upgrade1 = models.IntegerField()
