
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')# this mark - to make the last task have been added in the top of the list
    context = {'tasks': tasks}
    return render(request,'home.html',context)