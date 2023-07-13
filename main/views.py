from django.shortcuts import render, redirect
from .forms import Task_Create, Task_Update
# Create your views here.
from .models import Task


def home(request):
    form = Task_Create()
    tasks = Task.objects.all()
    if request.method == "POST":
        form = Task_Create(request.POST)
        if form.is_valid():
            print("ffff")
            form.save()
    
    if request.method == "GET":
        search = request.GET.get("q")
        print(search)
        if search is not None:
            
            tasks = Task.objects.filter(title__icontains=str(search))
        else:
            tasks = Task.objects.all()
    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request, 'index.html', context= context)


def update_task(request, id):
    instance = Task.objects.get(id = id)
    form = Task_Update(instance=instance)
    if request.method == "POST":
        form = Task_Update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("home")
            
            
    context = {
        "form":form
    }
    
    return render(request, 'update_task.html', context = context)


def delete_task(request, id):
    instance = Task.objects.get(id = id)
   
    if request.method == "POST":
        instance.delete()
        
        return redirect("home")
            
    context = {
        "task":instance
    }
    return render(request, 'delete_task.html', context=context)

