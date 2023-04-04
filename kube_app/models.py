from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileData(models.Model):
    ''' created database fields'''
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    class Meta:
        db_table = "profile_data"

