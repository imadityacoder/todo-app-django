from django.shortcuts import render,redirect
from .models import Todo





# Create your views here.
def home(request):
    if request.method == "POST":
        todotitle=request.POST.get("todotitle")
        tododesc=request.POST.get("tododesc")
        if todotitle == '' or tododesc == "":
            pass
        else:
            todo = Todo(title=todotitle,desc=tododesc)
            todo.save()
    
    todoget = Todo.objects.all()
    data = {'todoget':todoget}

    return render(request,"home.html",data)

def delete(request,id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('home')

  



 