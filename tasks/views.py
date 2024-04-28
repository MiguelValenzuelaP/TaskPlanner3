from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from .models import Task
from django.shortcuts import render


# Create your views here.
class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


def signUp(request):
    return render(request, "signup.html")
