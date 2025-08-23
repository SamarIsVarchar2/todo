from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display= ('task_descriptoin','is_completed','updated_at')
    search_fields=('task_descriptoin',)
admin.site.register(Task,TaskAdmin)
# Register your models here.
