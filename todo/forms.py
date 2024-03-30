from django import forms
from .models import Task


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Task
        fields = ("title",)
