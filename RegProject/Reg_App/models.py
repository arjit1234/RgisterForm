from django.db import models

# Create your models here.

class RegisterData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    mobile=models.BigIntegerField()

