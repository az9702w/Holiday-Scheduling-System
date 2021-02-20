from django.shortcuts import render, redirect
from BookHolidays.models import Staff
from django.contrib import messages

# This bookholidays function grabs the value from Book Holidays page.
def constraint_checker(request):
    if request.method == 'POST':
        #Getting the dates provided by the user.
        start_date = request.POST['start_date']
        end_date   =   request.POST['end_date']
        purposed_last_day  =   request.POST['last_date']
        print("Hello")
        if start_date  == end_date:
            messages.error(request, "Please provide different dates in order to book holidays")
        else:
            return "All good"

        

