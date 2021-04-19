from django.shortcuts import render, redirect
from BookHolidays.models import Staff
from django.contrib import messages
from datetime import datetime
from .models import Staff,Holidays_request
from accounts.models import Account




total_junior_staff_holidays = 23
total_senior_staff_holidays = 27
total_manager_holidays = 30
initial_holidays_taken = 0


'''This function checks number of staff in one departement (in database)
 are not exceeding the limit that we have defined as our constraint.'''
# maximum capacity of the departments being checked
def const_department_max_limit_checker(first_name,last_name,email,username,sl,dep,request):
    if request.method == 'POST':
        department = request.POST['department']
        staff_level = request.POST['level']
        if department == 'Cyber Security':
            if (staff_level == "Senior"):
                if Account.objects.filter(department="Cyber Security",level="Senior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  "in the department")
                    return False
            elif (staff_level == "Junior"):
                if Account.objects.filter(department="Cyber Security", level="Junior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  " staff in the department.")
                    return False
            elif (staff_level == "Line Manager") :
                if Account.objects.filter(department="Cyber Security",level="Line Manager").count()>0:
                    messages.error(request,"You already have one manager.")
                    return False
            elif (staff_level == "Assistant Line Manager"):
                if Account.objects.filter(department="Cyber Security", level="Assistant Line Manager").count()>0:
                    messages.error(request,"You already have assistant manager.")
                    return False
            else:
                print('success')
        elif department == 'Finance':
            if (staff_level == "Senior"):
                if Account.objects.filter(department="Finance",level="Senior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  " staff in the department")
                    return False
            elif (staff_level == "Junior"):
                if Account.objects.filter(department="Finance", level="Junior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  " staff in the department.")
                    return False
            elif (staff_level == "Line Manager") :
                if Account.objects.filter(department="Finance",level="Line Manager").count()>0:
                    messages.error(request,"You already have one manager.")
                    return False
            elif (staff_level == "Assistant Line Manager"):
                if Account.objects.filter(department="Finance", level="Assistant Line Manager").count()>0:
                    messages.error(request,"You already have assistant manager.")
                    return False
            else:
                print('success')
        elif department == 'Web Development Team':
            if (staff_level == "Senior"):
                if Account.objects.filter(department="Web Development Team",level="Senior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  "in the department")
                    return False
            elif (staff_level == "Junior"):
                if Account.objects.filter(department="Web Development Team", level="Junior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  " staff in the department.")
                    return False
            elif (staff_level == "Line Manager") :
                if Account.objects.filter(department="Web Development Team",level="Line Manager").count()>0:
                    messages.error(request,"You already have one manager.")
                    return False
            elif (staff_level == "Assistant Line Manager"):
                if Account.objects.filter(department="Web Development Team", level="Assistant Line Manager").count()>0:
                    messages.error(request,"You already have assistant manager.")
                    return False
            else:
                print('success')
        elif department == 'Backend Team':
            if (staff_level == "Senior"):
                if Account.objects.filter(department="Backend Team",level="Senior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  " in the department")
                    return False
            elif (staff_level == "Junior"):
                if Account.objects.filter(department="Backend Team", level="Junior").count()>4:
                    messages.error(request,"You have exceeded the max limit of number of " + staff_level +  "in the department.")
                    return False
            elif (staff_level == "Line Manager") :
                if Account.objects.filter(department="Backend Team",level="Line Manager").count()>0:
                    messages.error(request,"You already have one manager.")
                    return False
            elif (staff_level == "Assistant Line Manager"):
                if Account.objects.filter(department="Backend Team", level="Assistant Line Manager").count()>0:
                    messages.error(request,"You already have assistant manager.")
                    return False
            else:
                print('success')
    return True




# This function is defining maximum holidays for different staff levels and saving them in Staff table in database.
def max_holidays(username,first_name): 

    staff = Account.objects.get(username=username)
    if staff.level == "Junior":
        if Staff.objects.filter(first_name=first_name).exists():
            return 
        else:
            holidays_stats = Staff.objects.create(first_name=staff.first_name,last_name=staff.last_name,department=staff.department, staff_level=staff.level,
            Holidays_taken=initial_holidays_taken,Holidays_left=total_junior_staff_holidays)
            holidays_stats.save
    elif staff.level == "Senior":
        if Staff.objects.filter(first_name=first_name).exists():
            return
        else:
            holidays_stats = Staff.objects.create(first_name=staff.first_name,last_name=staff.last_name,department=staff.department, staff_level=staff.level,
            Holidays_taken=initial_holidays_taken,Holidays_left=total_senior_staff_holidays)
            holidays_stats.save
    elif staff.level == "Assistant Line Manager" or staff.level == "Line Manager":
        if Staff.objects.filter(first_name=first_name).exists():
            return
        else:
            holidays_stats = Staff.objects.create(first_name=staff.first_name,last_name=staff.last_name,department=staff.department, staff_level=staff.level,
            Holidays_taken=initial_holidays_taken,Holidays_left=total_manager_holidays)
            holidays_stats.save




