from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



def othertypes(request):
    return render(request, 'pages/OtherTypes.html')
def maternity(request):
    return render(request, 'pages/Maternity.html')
def paternity(request):
    return render(request, 'pages/Paternity.html')
def bookholidays(request):
    return render(request, 'pages/BookHolidays.html')
def accounts(request):
    return render(request, 'pages/Account.html')
