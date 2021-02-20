from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date   = models.DateField()
    last_working_day = models.DateField()
    staff_level = models.CharField(max_length=50)


