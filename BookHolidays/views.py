from django.shortcuts import render, redirect, HttpResponseRedirect
from   .utils import input_names, input_dates, feedback
from accounts.models import Account
from django.contrib.auth.decorators import login_required


# This bookholidays function returns the constraint_checker function from utils.py.

def accounts(request):
     input_names(request)
     return render(request, 'pages/register.html')

@login_required(login_url='/login/')     
def different_dates(request):
     input_dates(request)
     feedback(request)
     return render(request, 'pages/BookHolidays.html')