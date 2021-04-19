from django.shortcuts import render, redirect
from BookHolidays.models import Staff
from django.contrib import messages
from datetime import datetime
from .models import Staff,Holidays_request
from accounts.models import Account

total_junior_staff_holidays = 23
total_senior_staff_holidays = 27
total_manager_holidays = 30 




# maximum capacity of the departments being checked
def input_names(request):
     if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email     =request.POST['email']
        username  = request.POST['username']
        staff_level = request.POST['staff_level']
        department = request.POST['department']
        staff_note = request.POST['note_area']
        
        

# This function checks the dates provided are different and 
def input_dates(request):
    if request.method == 'POST':
    #Getting the dates provided by the user.
        start_date = request.POST['start_date']
        end_date   =  request.POST['end_date']
        staff_note = request.POST['note_area']
        username = request.user.username
        firstname = request.user.first_name 
        if holidays_left(start_date,end_date,request,username,firstname,staff_note):
            return redirect('bookholidays/')





#This checks the dates being provided are different.
def const_date_checker(start_date,end_date,request):
    if  start_date  == end_date: 
        messages.error(request, "Please provide different dates in order to book holidays")
        return False
    return True

      

'''This function checks if the new request maker is providing the holidays more than he/she has left.
 Then based on that, request is being saved in Holiday_request table in database.
'''
def holidays_left(start,end,request,username,first_name,staff_note): 
    #Formatting date coming from HTML form to date type in python.
     formatted_start_date = datetime.strptime(start, '%Y-%m-%d').date()     
     formatted_end_date = datetime.strptime(end, '%Y-%m-%d').date()  
     holidays_requested = (formatted_end_date - formatted_start_date).days
     print("The difference is " + str(holidays_requested)) 
     #calling Account table from DB to get attributes of employees.
     staff = Account.objects.get(username=username)
     #calling Staff table from DB to check holidays taken and left.
     holiday_stat = Staff.objects.get(first_name=first_name) 
     #This 'if' block is for the junior level staff 
     if staff.level == "Junior":          
        if holiday_stat.Holidays_left <= 0 or holidays_requested > holiday_stat.Holidays_left or holidays_requested > total_junior_staff_holidays:
            messages.error (request, "Cannot be booked .")
        elif const_date_checker(start,end,request) == False:
            return redirect('bookholidays')
        elif past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('bookholidays')
        else:
            #If request with same dates is submitted twice a person will get error message.
            same_dates_twice(staff.first_name,staff.last_name,staff.level,staff.department,start,end,request,staff_note) 
     elif staff.level == "Senior":          
        if holiday_stat.Holidays_left <= 0 or holidays_requested > holiday_stat.Holidays_left or holidays_requested > total_senior_staff_holidays:
            messages.error (request, "Cannot be booked.")
        elif const_date_checker(start,end,request) == False:
            return redirect('bookholidays')
        elif past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('bookholidays')
        else:
            #If request with same dates is submitted twice a person will get error message
            same_dates_twice(staff.first_name,staff.last_name,staff.level,staff.department,start,end,request,staff_note)
     elif staff.level == "Line Manager":          
        if holiday_stat.Holidays_left <= 0 or holidays_requested > holiday_stat.Holidays_left or holidays_requested > total_manager_holidays:
            messages.error (request, "Cannot be booked.")
        elif const_date_checker(start,end,request) == False:
            return redirect('bookholidays')
        elif past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('bookholidays')
        else:
            #If request with same dates is submitted twice a person will get error message
            same_dates_twice(staff.first_name,staff.last_name,staff.level,staff.department,start,end,request,staff_note) 
     elif staff.level == "Assistant Line Manager":          
        if holiday_stat.Holidays_left <= 0 or holidays_requested > holiday_stat.Holidays_left or holidays_requested > total_manager_holidays:
            messages.error (request, "Cannot be booked.")
        elif const_date_checker(start,end,request) == False:
            return redirect('bookholidays')
        elif past_dates(formatted_start_date,formatted_end_date,request) == False:
            return redirect('bookholidays')
        else:
            #If request with same dates is submitted twice a person will get error message
            same_dates_twice(staff.first_name,staff.last_name,staff.level,staff.department,start,end,request,staff_note)              
        # Calling holiday request table to grab its attributes
            #holiday_req_table = Holidays_request.objects.get(First_name=staff.first_name,Staff_level=staff.level,Department=staff.department)
            #max_people_off_in_dep(holiday_req_table.First_name,holiday_req_table.Staff_level,holiday_req_table.Department,start,end,request)
   
            
            #Processing the request - based on the constraints (3 staff must be present in the office.)
            #constraint_checking(holiday_req_table.First_name,holiday_req_table.Staff_level,holiday_req_table.Department,start,end)
                    #holidays_taken = Staff.Holidays_taken + holidays_requested
                    #holidays_left  =total_junior_staff_holidays - holidays_taken
            #constraint_checking(first_name,start,end)
        return True


#Displays error when same dates are submitted twice otherwise request is submitted in the DB.
def same_dates_twice(first_name,last_name,staff_level,department,start,end,request,staff_note):
    formatted_start_date = datetime.strptime(start, '%Y-%m-%d').date()     
    formatted_end_date = datetime.strptime(end, '%Y-%m-%d').date()  
    holidays_requested = (formatted_end_date - formatted_start_date).days 
    if Holidays_request.objects.filter(First_name=first_name,Last_name=last_name, Staff_level=staff_level, Department=department,
        start_date=start,end_date=end).exists():
        messages.error(request,"You already have one request with provided dates.")
        return redirect('bookholidays/'),False 
        #if same starting date or ending date is provided.
    elif (Holidays_request.objects.filter(start_date=start).exists() or Holidays_request.objects.filter(end_date=end).exists()):
        if Holidays_request.objects.filter(First_name=first_name,Last_name=last_name).exists():
            messages.error(request,"You already have one request.")
            return redirect('bookholidays/'),False  
        else:
            holiday_request = Holidays_request.objects.create(First_name=first_name,Last_name=last_name,Staff_level=staff_level, Department=department,
            start_date=start,end_date=end, staff_note_area=staff_note)
            holiday_request.save
            messages.success(request,"request submitted!")
            print("we got success!")
            max_people_off_in_dep(department,staff_level,start,end,request)
            #feedback(request)
    else:
                holiday_request = Holidays_request.objects.create(First_name=first_name,Last_name=last_name,Staff_level=staff_level, Department=department,
                start_date=start,end_date=end,staff_note_area=staff_note )
                holiday_request.save       
                messages.success(request,"request submitted!!!!!!")
                print("we got success!!!!!")
                max_people_off_in_dep(department,staff_level,start,end,request)
                #feedback(request)              
    return True

def max_people_off_in_dep(department,staff_level,start,end,request):
    if request.method == "POST":
        first_name = request.user.first_name 
        last_name = request.user.last_name 
        formatted_start_date = datetime.strptime(start, '%Y-%m-%d').date()     
        formatted_end_date = datetime.strptime(end, '%Y-%m-%d').date()
        holidays_requested = (formatted_end_date - formatted_start_date).days 

        if Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=start,end_date=end).count() > 2:   
            messages.error(request,"No, you cannot!!")
            #Provide alternatives here, if the dates provided cannot be booked.
            alternatives(staff_level,department,start,end,request) 
            return redirect('bookholidays/')
        elif (Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=start).exists() or
            Holidays_request.objects.filter(Staff_level=staff_level,Department=department,end_date=end).exists()) and (Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=start).count() > 2 or
            Holidays_request.objects.filter(Staff_level=staff_level,Department=department,end_date=end).count() > 2):
            messages.error(request,"Overlapping dates.")
            #Provide alternatives here, if the dates provided cannot be booked.
            # alternatives(staff_level,department,start,end,request) 
            overlapping(staff_level,department,start,end,request)
            return redirect('bookholidays/')
        elif Holidays_request.objects.filter(Staff_level=staff_level,Department=department, approved=True).count()>=2:
            overlapping(staff_level,department,start,end,request)
        else:            
            Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=formatted_start_date,end_date=formatted_end_date).update(approved=True)
            #Update Staff table in DB with Holidays taken and left.
            get_staff = Staff.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
            Staff.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level).update(Holidays_taken=get_staff.Holidays_taken+holidays_requested,Holidays_left=get_staff.Holidays_left-holidays_requested) 
            print("count is below or equal to two")
        return True
     

def overlapping(staff_level,department,start,end,request):
    formatted_start_date = datetime.strptime(start, '%Y-%m-%d').date()     
    formatted_end_date = datetime.strptime(end, '%Y-%m-%d').date()
    first_name = request.user.first_name 
    last_name = request.user.last_name 
    holidays_requested = (formatted_end_date - formatted_start_date).days 

    holiday_requests = Holidays_request.objects.filter(Staff_level=staff_level,Department=department, approved=True)
    count = 0
    for hr in  holiday_requests:
        if (hr.start_date <= formatted_start_date and formatted_start_date <=hr.end_date):
            count +=1  
            print('Dates fall in already booked date..............')
            if count >= 2:
                alternatives(staff_level,department,start,end,request)
                Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=formatted_start_date,end_date=formatted_end_date).update(approved=False)
                return False
        else:
            Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=formatted_start_date,end_date=formatted_end_date).update(approved=True)
            get_staff = Staff.objects.get(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level)
            Staff.objects.filter(first_name=first_name,last_name=last_name,department=department,staff_level=staff_level).update(Holidays_taken=get_staff.Holidays_taken+holidays_requested,Holidays_left=get_staff.Holidays_left-holidays_requested)
            print("Come in else block.")
        
    return True, ('bookholidays/')


#if provided dates are not booked, suggest alternatives.
def alternatives(staff_level,department,start,end,request):
    if request.method == "POST":
        first_name = request.user.first_name 
        last_name = request.user.last_name 
        formatted_start_date = datetime.strptime(start, '%Y-%m-%d').date()     
        formatted_end_date = datetime.strptime(end, '%Y-%m-%d').date()
        holidays_requested = (formatted_end_date - formatted_start_date)
        suggested_start_date = formatted_start_date + holidays_requested
        suggested_end_date   = formatted_end_date + holidays_requested
        if Holidays_request.objects.filter(Staff_level=staff_level,Department=department,approved=True).count() >= 2:
                print(first_name + ", Here's your alternatives: suggested start date: " + str(suggested_start_date) + " suggested end date: " +  str(suggested_end_date))
                messages.error(request, first_name + " Here's your alternative Suggested start date: " + str(suggested_start_date) + " Suggested end date: " + str(suggested_end_date))
                return redirect('bookholidays/')                
                #Update Staff table in DB with Holidays taken and left.
        else:         
             Holidays_request.objects.filter(Staff_level=staff_level,Department=department,start_date=formatted_start_date,end_date=formatted_end_date).update(approved=True)
             print("no overlaps")
    return True

#ensure the dates are not in the past. 
def past_dates(start,end,request):
    present = datetime.now().date()
    if (start < present or end < present or start > end) or (start == end):
        messages.error(request,"Dates are invalid!")
        return False
    elif (start - present).days < 7:
        messages.error(request,"Please allow us one week to process your request.")
        return False
    return True



 






        
