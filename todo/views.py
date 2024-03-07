from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import TaskUpdateForm
from .models import Task

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class TaskListView(LoginRequiredMixin,generic.ListView):
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 2

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).order_by('-datetime_created')

class TaskDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskCreateView(LoginRequiredMixin,generic.CreateView):
    model = Task
    fields = ["title"]
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo:task-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView,self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskUpdateForm
    template_name = "todo/task_update.html"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskDeleteView(LoginRequiredMixin,generic.DeleteView):
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_delete.html"
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskDoneView(LoginRequiredMixin,generic.View):    
    model = Task
    success_url = reverse_lazy("todo:task-list")

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs.get("pk"))
        task.is_done = True
        task.save()
        return redirect(self.success_url)

class TaskUndoView(LoginRequiredMixin,generic.View):
    model = Task
    success_url = reverse_lazy("todo:task-list")

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs.get("pk"))
        task.is_done = False
        task.save()
        return redirect(self.success_url)