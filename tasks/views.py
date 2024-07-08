from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from tasks.forms import TaskForm
from tasks.models import Task
from users.models import CustomUser
from django.contrib import messages

# Create your views here.
def showtaskformdata(request):
    if request.method == 'POST':
        fm = TaskForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Task Added Successfully!')
            title = fm.cleaned_data['title']
            description = fm.cleaned_data['description']
            date = fm.cleaned_data['date']
            is_completed = fm.cleaned_data['is_completed']
            user = request.user
            task = Task(title=title,description=description,date=date,is_completed=is_completed,user=user)
            task.save()
    else:
        fm = TaskForm()
    return render(request,"tasks/showtask.html",{"form":fm})    

def showtasksummary(request):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser, username=request.user.username)
        sum = Task.objects.filter(user=user)
        return render(request, 'tasks/tasksummary.html', {'summary':sum})
    else:
        return HttpResponseRedirect('/user/login/')

def update_task(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        fm = TaskForm(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= Task.objects.get(pk=id)
        fm = TaskForm(instance= pi)
    return render(request, 'tasks/updatetask.html',{'form':fm})

def delete_task(request, id):
    if request.method == "POST":
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/tasks/home')