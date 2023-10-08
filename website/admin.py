from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task, TaskType, Note, NoteImage


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Note)
admin.site.register(NoteImage)
