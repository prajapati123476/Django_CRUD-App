import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app import models

# Create your views here.

def index(request):
    s = "hello world"
    return HttpResponse(s)

def insert(request):
    s = render(request, 'app/index.html')
    return s

def saveStdent(request):
    # if request.method == "POST":
    student = models.Student()

    student.sname = request.POST['sname']
    student.srno = request.POST['srno']
    student.ssec = request.POST['ssec']
    student.scourse = request.POST['scourse']
    # print("submitted")
    student.save()
    return HttpResponseRedirect('http://localhost:8000/app/view')

def viewStudent(request):
    student = models.Student.objects.all()
    # d = {'student': student}
    res = render(request, 'app/index.html', {'student': student})
    return res
