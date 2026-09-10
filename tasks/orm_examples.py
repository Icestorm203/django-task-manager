from tasks.models import Task

def demo_orm():
    # Create
    task = Task.objects.create(title="Test", description="Demo")
    print("Создана задача:", task.id)

    # Read
    tasks = Task.objects.all()
    print("Всего задач:", tasks.count())

    # Update
    task.is_closed = True
    task.save()
    print("Задача обновлена:", task.id)

    # Delete
    task.delete()
    print("Задача удалена:", task.id)
