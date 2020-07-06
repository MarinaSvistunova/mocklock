from django.db import models
from django.contrib.auth.models import User


class TaskToDo(models.Model):
    task = models.CharField(max_length=200, default='New task')
    user = models.ForeignKey(User, default=id(0), on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f'{self.task}'