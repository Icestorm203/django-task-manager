from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):

    status = request.GET.get('status')

    tasks = Task.objects.all().order_by('-created_at')

    if status == 'open':
        tasks = tasks.filter(is_closed=False)

    elif status == 'closed':
        tasks = tasks.filter(is_closed=True)

    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks,
            'current_status': status
        }
    )

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description
        )

        return redirect('task_list')

    return render(request, 'tasks/create_task.html')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('task_list')


def close_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_closed = True
    task.save()

    return redirect('task_list')


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_closed = not task.is_closed

    task.save()

    return redirect('task_list')