from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student
from .models import Emoloyee

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def myform(request):
    return render(request,'myform.html')

class studentlist(ListView):
    model = Student
    template_name = 'slist.html'

class employeelist(ListView):
    model = Emoloyee
    template_name = 'elist.html'


def process(request):
    print('Welcome')
    print(request.method)
    print(request.POST)
    name  = request.POST['name']
    email  = request.POST['email']
    password = request.POST['password']
    age = int(request.POST['age'])
    phone = int(request.POST['phone'])
    dob = request.POST['dob']
    gender = request.POST['gender']
    city = request.POST['city']
    skill = request.POST['skill']
    sem = request.POST['sem']
    return render(
        request,"ans.html",{
            'myname':name,
            'myemail':email,
            'mypassword':password,
            'myage':age,
            'myphone':phone,
            'mydob':dob,
            'mygender':gender,
            'mycity':city,
            'myskill':skill,
            'mysem':sem,
        })

