from django.db import models
from django.db.models import Model

# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField(max_length=13)
    pan_card = models.CharField(max_length=12)
    