from django.db import models

# Create your models here.

class dream112(models.Model):
  
  phone = models.CharField(max_length=10)
  passw = models.CharField(max_length=10)