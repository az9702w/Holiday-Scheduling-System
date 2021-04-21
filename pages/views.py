from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from accounts.models import Account
from   BookHolidays.utils import past_dates
from datetime import datetime
from django.contrib import messages
from .models import Leaves_request
from BookHolidays.models import Staff, Holidays_request
from django.contrib.auth.decorators import login_required





@login_required(login_url='/login/')
def othertypes(request):
    argss = None
    if request.method == 'POST':
        subject = "Paternity Leaves request"
        email = request.user.email
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        sender = str(email)
        
        #getting dates from form
        start_date = request.POST['start_date']
        end_date   =  request.POST['end_date']
        staff_note = request.POST['note_area']
        #formattted dates
        formatted_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()     
        formatted_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        #checking invalid dates are not being provided
        if past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('OtherTypes') 
        else:
            if (Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level, start_date=start_date,end_date=end_date).exists()) and not(formatted_start_date < datetime.now().date()):
                     messages.error(request,"You already have a request.")
                     response = Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)                      
                     argss = {'res' : response}
                     print(response.admin_note_area)                 
            else:
                messages.success(request, "Your leave request is submitted. ")
                leaves_request = Leaves_request.objects.create(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level,start_date=start_date,end_date=end_date,staff_note_area=staff_note)
                leaves_request.save
                 # sending email is commented out
                '''send_mail(
            subject,
            str(formatted_start_date) + " and end_date: " + str(formatted_end_date),
            sender,         
            ['abdullahzulfiqar110@gmail.com'],
            fail_silently=False,
        )'''
    if request.method == "GET":
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        if Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level).exists():
            get_feedback= Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
            if not(get_feedback.admin_note_area == None):
                response = Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
                argss = {'res' : response}
                print(response.admin_note_area)
    return render(request, 'pages/OtherTypes.html',argss)

@login_required(login_url='/login/')
def maternity(request):
    argss = None
    if request.method == 'POST':
        subject = "Maternity Leaves request"
        email = request.user.email
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        sender = str(email)
        
        #getting dates from form
        start_date = request.POST['start_date']
        end_date   =  request.POST['end_date']
        staff_note = request.POST['note_area']
        #formattted dates
        formatted_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()     
        formatted_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        #checking invalid dates are not being provided
        if past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('MaternityLeaves') 
        else:
            if (Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level, start_date=start_date,end_date=end_date).exists()) and not(formatted_start_date < datetime.now().date()):
                     messages.error(request,"You already have a request.")
                     response = Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)                      
                     argss = {'res' : response}
                     print(response.admin_note_area)                 
            else:
                messages.success(request, "Your leave request is submitted. ")
                leaves_request = Leaves_request.objects.create(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level,start_date=start_date,end_date=end_date,staff_note_area=staff_note)
                leaves_request.save
                 # sending email is commented out
                '''send_mail(
            subject,
            str(formatted_start_date) + " and end_date: " + str(formatted_end_date),
            sender,         
            ['abdullahzulfiqar110@gmail.com'],
            fail_silently=False,
        )'''
    if request.method == "GET":
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        if Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level).exists():
            get_feedback= Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
            if not(get_feedback.admin_note_area == None):
                response = Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
                argss = {'res' : response}
                print(response.admin_note_area)
    return render(request, 'pages/Maternity.html',argss)

@login_required(login_url='/login/')
def paternity(request):
    argss = None
    if request.method == 'POST':
        subject = "Paternity Leaves request"
        email = request.user.email
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        
        #getting dates from form
        start_date = request.POST['start_date']
        end_date   =  request.POST['end_date']
        staff_note = request.POST['note_area']
        #formattted dates
        formatted_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()     
        formatted_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        #checking invalid dates are not being provided
        if past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('PaternityLeaves') 
        else:
            if (Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level, start_date=start_date,end_date=end_date).exists()) and not(formatted_start_date < datetime.now().date()):
                     messages.error(request,"You already have a request.")
            else:
                messages.success(request, "Your leave request is submitted. ")
                leaves_request = Leaves_request.objects.create(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level,start_date=start_date,end_date=end_date,staff_note_area=staff_note)
                leaves_request.save
       # sending email is commented out
                '''send_mail(
            subject,
            str(formatted_start_date) + " and end_date: " + str(formatted_end_date),
            sender,         
            ['abdullahzulfiqar110@gmail.com'],
            fail_silently=False,
        )'''
    if request.method == "GET":
        first_name= request.user.first_name
        last_name= request.user.last_name
        department = request.user.department
        staff_level =request.user.level
        if Leaves_request.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level).exists():
            get_feedback= Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
            if not(get_feedback.admin_note_area == None):
                response = Leaves_request.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
                argss = {'res' : response}
                print(response.admin_note_area)
        

    return render(request, 'pages/Paternity.html', argss)

@login_required(login_url='login/')
def bookholidays(request):
    return render(request, 'pages/BookHolidays.html')

@login_required(login_url='/pages/login/')   
def accounts(request):
    return render(request, 'pages/Account.html')




@login_required(login_url='/login/')
def history(request):
    first_name= request.user.first_name
    last_name= request.user.last_name
    department = request.user.department
    staff_level =request.user.level

    
    if Holidays_request.objects.filter(First_name=first_name,Last_name=last_name,Department=department,Staff_level=staff_level, approved=True).exists():
        get_staff = Staff.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
        get_approved_requests = Holidays_request.objects.filter(First_name=first_name,Last_name=last_name,Department=department,Staff_level=staff_level, approved=True)
        update_dates = {"update_history" : get_staff, "approved_dates": get_approved_requests}
    else:
        update_dates = {"update_history" : None, "approved_dates": None}

    return render(request, 'pages/Holiday_history.html', update_dates)

