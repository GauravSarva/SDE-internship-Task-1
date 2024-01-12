from django.shortcuts import render
from django.http import HttpResponse

def ui(request):
    return HttpResponse("This is the first page")

def task(request):
    dynamic_data = "Hello, this is dynamic data!"
    return render(request, 'task.html', {'dynamic_data': dynamic_data})
