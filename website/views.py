from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Services

# Create your views here.


def index(request):
    items = Services.objects.all()
    data = {'page_name':'Home', 'items' : items}
    return render(request, 'index.html',data)


def serviceDetails(request , param):
    data = {'page_name':'Service details'}
    item = Services.objects.get(id=param)
    data.update({'item':item})
    
    return render(request, 'service-details.html',data)

def portfolioDetails(request):
    data = {'page_name':'Portfolio details'}
    
    return render(request, 'portfolio-details.html', data)

def register(request):
    data = {'page_name':'Register'}
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        
        if password==conf_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                messages.info(request, 'Registeration successfull!')
                user.save()
                return redirect('register')
        else:
            messages.info(request, 'Password not same!')
            return redirect('register')
            
    return render(request, 'register.html', data)

def login(request):
    data = {'page_name':'Login'}
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials not matched!')

    return render(request, 'login.html',data)

def logout(request):
    auth.logout(request)
    return redirect('login')