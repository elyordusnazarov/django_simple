from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages



def home(request):
    return render(request,'home.html', {'title':'Home Page'})

def addPage(request):
    return render(request, 'addform.html')

def add(request):
    
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))

    result = val1 + val2

    return render(request, 'result.html', {'result':result})


def register(request):
    if request.method == 'POST':        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email Taken')
               return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('login')            
            
    else:    
        
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request,username=username,password=password)

        if user is not None:           
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')


    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')



    




    





