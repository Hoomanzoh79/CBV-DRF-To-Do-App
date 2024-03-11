from .serializers import TaskSerializer
from todo.models import Task
from rest_framework import viewsets
# from .permissions import IsOwnerPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from .paginations import DefaultPagination


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(is_done=False)

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {"author": ["exact", "in"]}
    search_fields = ["title"]
    ordering_fields = ["datetime_created"]
