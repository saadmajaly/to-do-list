from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    tasks=Task.objects.all()
    
    return render(request,"Task/index.html",{"tasks":tasks})
def addtemp(request):
    
    return render(request,"Task/add.html")
@csrf_exempt

def add(request):
    title=request.POST["title"]
    date=request.POST["date"]
    description=request.POST["desc"]
    task = Task(taskTitle=title,dueDate=date,taskDescription=description)
    task.save()
    return redirect("/")

def edittemp(request,id):
    edtask=Task.objects.get(id=id)
    return render(request,"Task/edit.html",{'task':edtask})

def edit(request,id):
    edtask=Task.objects.get(id=id)
    edtask.taskTitle=request.POST["title"]
    edtask.dueDate=request.POST["date"]
    edtask.taskDescription=request.POST["desc"]
    edtask.save()
    return redirect("/")

def deleteT(request,id):
    delTask=Task.objects.get(id=id)
    delTask.delete()
    return redirect("/")