from django.db import models
from django.utils import timezone
from datetime import date

from users.models import CustomUser


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=date.today)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_task"
    )

    def __str__(self):
        return self.title
