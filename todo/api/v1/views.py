from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TaskSerializer
from todo.models import Task
from .paginations import DefaultPagination
from .permissions import IsOwnerPermission


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(status=True)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"author": ["exact", "in"]}
    search_fields = ["title"]
    ordering_fields = ["datetime_created"]
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]
