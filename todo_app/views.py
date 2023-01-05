from django.shortcuts import render
from django.http import HttpResponse
from . models import Task
# Create your views here.
def task_view(request):
    obj1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = Task(name=name, priority=priority)
        obj.save()
    # return HttpResponse("rr")
    return render(request,'task_view.html',{'obj1':obj1})

# def task(request):
#     if request == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name=name, priority=priority)
#         obj.save()
#     return render(request,'task.html')