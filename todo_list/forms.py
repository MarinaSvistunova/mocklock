from django.forms import ModelForm

from .models import TaskToDo


class SaveTask(ModelForm):
    class Meta:
        model = TaskToDo
        fields = ["task"]