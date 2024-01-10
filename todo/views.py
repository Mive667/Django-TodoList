from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def add_task(request):
    task_str = request.POST["task"]
    Task.objects.create(
        task = task_str,
    )
    return redirect("index")