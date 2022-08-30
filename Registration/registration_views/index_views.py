from django.shortcuts import render
from django.urls import path


# Create your views here.
def index(request):
    return render(request, 'Registration/index.html')

index_template = [
    path('', index, name='index'),
]