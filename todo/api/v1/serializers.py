from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["author","id","title","is_done"]