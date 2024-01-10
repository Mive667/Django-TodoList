

from django.shortcuts import render
from todo.models import Task


def index(request):
    uncompleted_tasks = (
        Task.objects.
        filter(is_completed=False).
        order_by('-created_at')
        )
    completed_tasks = (
        Task.objects.
        filter(is_completed=True).
        order_by('updated_at')
        )
    context = {
        "completed_tasks": completed_tasks,
        "uncompleted_tasks": uncompleted_tasks,
    }
    return render(request, "todo_main/index.html", context)
