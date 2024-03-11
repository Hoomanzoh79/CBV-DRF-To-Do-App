from rest_framework import serializers
from todo.models import Task
from accounts.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "is_done",
            "author",
            "datetime_created",
            "absolute_url",
        ]
        read_only_fields = ["author"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = Profile.objects.get(user_id=request.user.id)
        return super().create(validated_data)

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context["kwargs"].get("pk"):
            rep.pop("id", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("is_done", None)

        return rep
