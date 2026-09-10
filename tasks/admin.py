import csv
from django.http import HttpResponseRedirect
from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from .models import Task
from .forms import TaskImportForm

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    verbose_name = "task"
    verbose_name_plural = "tasks"
    list_display = ("id", "title", "is_closed", "created_at")
    list_editable = ("is_closed",)
    list_filter = ("is_closed", "created_at")
    search_fields = ("title", "description")
    ordering = ("id",)
    list_per_page = 20

    actions = ["close_selected_tasks", "export_tasks_csv"]

    # --- Импорт CSV ---
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("import-csv/", self.import_csv, name="task_import_csv"),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            form = TaskImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data["csv_file"]
                decoded = csv_file.read().decode("utf-8").splitlines()
                reader = csv.DictReader(decoded)

                count = 0
                for row in reader:
                    Task.objects.create(
                        title=row.get("title", ""),
                        description=row.get("description", ""),
                        is_closed=row.get("is_closed", "False").lower() == "true",
                    )
                    count += 1

                self.message_user(request, f"Импортировано задач: {count}")
                return HttpResponseRedirect("../")

        else:
            form = TaskImportForm()

        return render(request, "admin/task_import_form.html", {"form": form})

    # --- Экспорт CSV ---
    def export_tasks_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="tasks_export.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID", "Title", "Description", "Is Closed", "Created At"])

        for task in queryset:
            writer.writerow([
                task.id,
                task.title,
                task.description,
                task.is_closed,
                task.created_at,
            ])

        return response

    export_tasks_csv.short_description = "Экспортировать выбранные задачи в CSV"

    # --- Закрытие задач ---
    def close_selected_tasks(self, request, queryset):
        updated = queryset.update(is_closed=True)
        self.message_user(request, f"Закрыто задач: {updated}")
    close_selected_tasks.short_description = "Закрыть выбранные задачи"
