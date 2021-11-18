from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def shwetha(request):
    return HttpResponse('HEY!! THIS IS SHWETHA ')

def sumit(request):
    return render(request,'app1/h1.html')    