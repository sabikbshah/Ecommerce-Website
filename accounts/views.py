from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib import messages

from .forms import LoginForm

# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request,"User Created Successfully!")
            return redirect('login')
        else:
            messages.error(request,"User Already Exist.")
            return render(request,'auth/register.html',{'form':regform})
            

    context = {
        'form': UserCreationForm
    }

    return render(request,'auth/register.html',context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        user = authenticate(username = username, password =  password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_staff:
                return redirect('/vendor/mystore')
            else:
                messages.success(request,f"welcome {user.username.upper()},Your Logged In.")
                return redirect('/')
        else:
            messages.error(request,'User not Found')
            return render(request, 'auth/login.html',{'form':LoginForm})
    context = {
        'form': LoginForm

    }
    return render(request,'auth/login.html',context)

def userlogout(request):

    logout(request)
    messages.success(request,'user Logged out')
    return redirect('/')