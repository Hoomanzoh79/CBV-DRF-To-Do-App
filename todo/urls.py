from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path('list/',views.TaskListView.as_view(),name='task-list'),
    path('list/<int:pk>/',views.TaskDetailView.as_view(),name='task-detail'),
]
