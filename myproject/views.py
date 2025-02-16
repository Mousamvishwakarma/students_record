from django.http import HttpResponse
from django.shortcuts import render
def home(request):
 
    return HttpResponse("hello gyan sagar")

def loginpage(request):
    return HttpResponse("welcome in login page")

def logoutpage(request):
    return HttpResponse("logout your page")

from .models import studentdata

def indexpage(request):
    if request.method =="POST":
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        temp = studentdata (name = firstname, email = email, address = address )
        temp.save()
    return render(request,'index.html')
