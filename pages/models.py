from django.db import models


# holidays stats
class Leaves_request(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    staff_level = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date   = models.DateField()
    staff_note_area = models.TextField(max_length=200)
    admin_note_area = models.TextField(max_length=200)
