from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from .models import Task


# Create your views here.
class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
