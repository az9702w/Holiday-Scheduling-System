from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from BookHolidays.models import Staff,User
from accounts.models import Account
from BookHolidays.Department_related_fun import const_department_max_limit_checker, max_holidays
# Create your views here.

def register(request):
    if request.method == 'POST':
        #Register-User Logic 
        #Get form values
        email = request.POST['email']
        username= request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        level = request.POST['level']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check if password matches
        if password == password2:
            #checking if user with current username already exists in the database
            if Account.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
            #checking if user with current email already exists in the database
                if Account.objects.filter(email=email).exists():
                    messages.error(request, "User already exists with this email address")
                    return redirect('register')
                    # This checks if a particular department has the number of employees equal to what we have defined as our constraint.
                elif const_department_max_limit_checker(first_name,last_name,email,username,level,department,request) == False:
                    return redirect('register')
                else:
                    #All Good-if user is providing an email and username
                    #which does not exist in the databae, then create a new user.
                    user = Account.objects.create_user(email=email, username=username, first_name=first_name,last_name=last_name, department=department,
                    level=level, password=password)
                    #after registeration users are directed to login page.
                    user.save()
                    messages.success(request, "You are now registered and can log in")
                    max_holidays(username,first_name)
                    return redirect('login')
                    

        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')




def login(request):
      if request.method == 'POST':
        #Login User Logic 
          email= request.POST['email']
          password= request.POST['password']
         #user is being authenticated
          user = auth.authenticate(email=email, password=password)
          if user is not None:
              auth.login(request,user)
              messages.success(request, "You are now logged in")
              return redirect("History")
          else: 
              messages.error(request,"invalid credentials")
              return redirect('login')

        
      else:
        return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are now logout")
        return render(request, 'pages/register.html')


