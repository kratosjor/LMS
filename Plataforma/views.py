from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

########################
#-----VIEW HOME
########################

def home(request):
    return render(request, 'home.html')