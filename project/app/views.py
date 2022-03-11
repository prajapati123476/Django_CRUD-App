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
	# return HttpResponseRedirect('http://localhost:8000/app/view')


def viewStudent(request):
    student = models.Student.objects.all()
    # d = {'student': student}
    res = render(request, 'app/index.html', {'student': student})
    return res


def updateStudent(request):
    std = models.Student.objects.get(id=request.GET['id'])
    res = render(request, 'app/updatestudent.html', {'std':std})
    return res

def update(request):
    std = models.Student()
    std.id = request.POST['id']
    std.sname = request.POST['sname']
    std.srno = request.POST['srno']
    std.ssec = request.POST['ssec']
    std.scourse = request.POST['scourse']
    std.save()
    return HttpResponseRedirect('http://localhost:8000/app/view')

def delete(request):
    stdnt = models.Student.objects.get(id = request.GET['id'])
    stdnt.delete()
    return HttpResponseRedirect('http://localhost:8000/app/view')
