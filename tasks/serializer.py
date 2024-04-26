from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        # fields = {"id", "title", "description", "done"}
        fields = "__all__"  # inicializa todo
