from django.core.management.base import BaseCommand
from tasks.models import Task

class Command(BaseCommand):
    help = "Закрывает все открытые задачи"

    def handle(self, *args, **kwargs):
        count = Task.objects.filter(is_closed=False).update(is_closed=True)
        self.stdout.write(self.style.SUCCESS(f"Закрыто задач: {count}"))
