from django.contrib import admin
from .models import Task

class names(admin.ModelAdmin):
  list_display = ("title", "status", "due_date", "created_at",)


admin.site.register(Task, names)


