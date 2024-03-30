from django.urls import path, include
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("list/", views.TaskListView.as_view(), name="task-list"),
    path("list/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("list/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("list/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("list/<int:pk>/done/", views.TaskDoneView.as_view(), name="task-done"),
    path("list/<int:pk>/undo/", views.TaskUndoView.as_view(), name="task-undo"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    # API
    path("api/v1/", include("todo.api.v1.urls")),
]
