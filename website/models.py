from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

import os

from django.contrib.auth.models import User

from django.conf import settings


# Функция для генерации пути для изображения
def user_directory_path(instance, filename):
    # Получаем имя пользователя и дату создания заметки
    user = instance.note.user.username
    date = instance.note.created_at.strftime("%Y/%m/%d")

    # Генерируем путь в формате "media/user1/2023/01/01/image.jpg"
    return f"media/{user}/{date}/{filename}"


class NoteImage(models.Model):
    # Связь с заметкой, к которой относится изображение
    note = models.ForeignKey(
        "website.Note", on_delete=models.CASCADE, related_name="note_images"
    )  # Обновлен related_name
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Image")


class CustomUser(AbstractUser):
    # Добавьте свои дополнительные поля пользователя
    birth_date = models.DateField(null=True, blank=True)
    # Другие поля...


class TaskType(models.Model):
    task_type = models.CharField(max_length=100)

    def __str__(self):
        return self.task_type


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Task Choice",
    )
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_time = models.DateTimeField(blank=True, verbose_name="Time of reminder")
    completion_time = models.DateTimeField(blank=True)
    is_done = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return f"{self.task_name} {self.task_type}"


class Note(models.Model):
    # Другие поля вашей модели Note
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # Произвольное количество картинок (необязательно)
    images = models.ManyToManyField(NoteImage, blank=True, related_name="notes")

    def __str__(self):
        return self.title
