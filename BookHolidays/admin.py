from django.contrib import admin

# Register your models here.
from .models import Staff,Holidays_request

admin.site.register(Staff)
admin.site.register(Holidays_request)