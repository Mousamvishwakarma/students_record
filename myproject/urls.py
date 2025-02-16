
from django.contrib import admin
from django.urls import path
from studentapp.views import  home,loginpage,logoutpage,indexpage 
urlpatterns = [ 
    path('',home),
    path('login/',loginpage),
    path('logout/',logoutpage),
    path('admin/', admin.site.urls),
    path('index/',indexpage)
    
]
