from django.shortcuts import render
from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.
def showtaskformdata(request):
    if request.method == 'POST':
        fm = TaskForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            description = fm.cleaned_data['description']
            date = fm.cleaned_data['date']
            is_completed = fm.cleaned_data['is_completed']
            user = fm.cleaned_data['user']
            task = Task(title=title,description=description,date=date,is_completed=is_completed,user=user)
            task.save()
    else:
        fm = TaskForm()
    return render(request,"tasks/showtask.html",{"form":fm})    