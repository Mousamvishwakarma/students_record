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

#def marsk(request):
#    if request.method =="POST":
#        sub1 = request.POST.get('sub1')
#        sub2 = request.POST.get('sub2')
#        sub3 = request.POST.get('sub3')
#        sub4 = request.POST.get('sub4')
#        sub5 = request.POST.get('sub5')
#
#        temp = Studentmarks (sub1 = sub1, sub2 = sub2, sub3 = sub3, sub4 = sub4, sub5 = sub5)
#        temp.save()
#    return render(request,'marks.html')