from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin,generic.ListView):
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskDetailView(LoginRequiredMixin,generic.DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'