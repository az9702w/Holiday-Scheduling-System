from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        #Register-User Logic 
        #Get form values
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password matches
        if password == password2:
            #checking if user with current username already exists in the database
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
            #checking if user with current email already exists in the database
                if User.objects.filter(email=email).exists():
                    messages.error(request, "User already exists with this email address")
                    return redirect('register')
                else:
                    #All Good-if user is providing an email and username
                    #which does not exist in the databae, then create a new user.
                    user = User.objects.create_user(email=email, password=password, username=username)
                    #after registeration users are directed to login page.
                    user.save()
                    messages.success(request, "You are now registered and can log in")
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
              return redirect("BookHolidays")
          else: 
              messages.error(request,"invalid credentials")
              return redirect('login')

        
      else:
        return render(request, 'pages/login.html')



def logout(request):
    return redirect(request, 'register')