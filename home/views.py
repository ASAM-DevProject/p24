from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login

from acc.models import ProfileSick

# Create your views here.

def home(request):
    
    if request.user.is_authenticated:
        profile = ProfileSick.objects.get(user=request.user)
        return render(request, 'home/home.html', {'profile':profile})
    else:
        return render(request, 'home/home.html')

def error_access_permission_dr(request):
    return render(request, 'error/not_authorization_dr.html')

def error_access_permission_sick(request):
    return render(request, 'error/not_authorization_sick.html')