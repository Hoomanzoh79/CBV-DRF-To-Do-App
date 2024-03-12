from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializer
from todo.models import Task
from .paginations import DefaultPagination
from .permissions import IsOwnerPermission
from accounts.models import Profile

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"author": ["exact", "in"]}
    search_fields = ["title"]
    ordering_fields = ["datetime_created"]
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated,IsOwnerPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.all()
        if user.is_superuser & user.is_staff:
            return queryset
        
        return queryset.filter(author=Profile.objects.get(user_id=user.id))
