from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(generic.ListView):
    queryset = Task.objects.filter(is_done=False)
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'