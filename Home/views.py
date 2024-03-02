from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime


# Create your views here.
def home(request):
    if request.method == "POST":
        todotitle=request.POST.get("todotitle")
        tododesc=request.POST.get("tododesc")
        if todotitle == '' or tododesc == "":
            pass
        else:
            todo = Todo(title=todotitle,desc=tododesc,date=datetime.now())
            todo.save()
    
    todoget = Todo.objects.all()
    data = {'todoget':todoget}

    return render(request,"home.html",data)

def delete(request,id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('home')

def update(request,id):
    t_update = request.POST.get('title')
    d_update = request.POST.get('desc')
    todo = Todo.objects.get(id = id)
  
    data = {"get": todo}

    return render(request,"update.html",data)


 