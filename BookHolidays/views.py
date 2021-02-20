from django.shortcuts import render, redirect, HttpResponseRedirect
from   .utils import constraint_checker


# This bookholidays function returns the constraint_checker function from utils.py.
def bookholidays(request):
     constraint_checker(request)
     return render(request, 'pages/BookHolidays.html')
# This accounts function grabs the value from Account.html page and store them in database
def accounts(request):
    #Getting the dates provided by the user and storing them in database.
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     return 