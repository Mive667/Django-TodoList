from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Task


# Create your views here.
def add_task(request):
    task_str = request.POST["task"]
    Task.objects.create(
        task = task_str,
    )
    return redirect("index")


def mark_as_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("index")


def mark_as_uncompleted(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("index")


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        # update task content
        edited_task_str = request.POST["edited_task"]
        task.task = edited_task_str
        task.save()
        return redirect("index")
    else:
        print(request.method)
        context = {
        'task': task,
        }
        return render(request, "todo/edit_task.html", context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")
