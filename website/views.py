from django.shortcuts import render
from django.http import HttpResponse
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