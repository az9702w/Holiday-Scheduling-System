from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account



# This class makes a table in database for holding record of holidays taken and left for all users.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    staff_level = models.CharField(max_length=100)
    Holidays_taken = models.IntegerField(null=True)
    Holidays_left= models.IntegerField(null=True)

# This class create all the fields in Database to save holiday requests of the users.
class Holidays_request(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Department =  models.CharField(max_length=100)
    Staff_level = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date   = models.DateField()
    staff_note_area = models.TextField(max_length=200)
    admin_note_area = models.TextField(max_length=200)
    approved = models.BooleanField(default=False)


