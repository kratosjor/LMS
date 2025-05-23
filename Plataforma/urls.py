from django.urls import path
from .views import *

paths = [
    path('', home, name='home'),
]