from django.db import models

# Create your models here.


class playerget(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_dateee = models.DateField(null=True)
