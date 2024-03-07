from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('list/',views.TaskListView.as_view(),name='task-list'),
    path('list/<int:pk>/',views.TaskDetailView.as_view(),name='task-detail'),
    path('list/<int:pk>/update/',views.TaskUpdateView.as_view(),name='task-update'),
    path('create/',views.TaskCreateView.as_view(),name='task-create'),
]
