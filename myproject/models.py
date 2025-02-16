from django.db import models

# Create your models here.
class studentdata(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField(max_length=50)

#class Studentmarks(models.Model):
   # sub1 = models.IntegerField() 
   # sub2 = models.IntegerField()
   # sub3 = models.IntegerField()
   # sub4 = models.IntegerField()
   # sub5 = models.IntegerField()