from datetime import datetime

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-is_active", "-created"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.content
