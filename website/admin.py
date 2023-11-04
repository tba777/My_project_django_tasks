from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Note, NoteImage, Task, TaskType


class CustomUserAdmin(UserAdmin):
    model = CustomUser    # type: ignore


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Note)
admin.site.register(NoteImage)
