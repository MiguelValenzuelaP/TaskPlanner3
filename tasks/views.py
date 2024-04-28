from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from .models import Task
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


def signUp(request):
    if request.method == "GET":
        print("Sending form")
        return render(request, "./signup.html", {"form": UserCreationForm})
    else:
        print("Getting data")
        if checkPassword(
            password1=request.POST["password1"], password2=request.POST["password2"]
        ):
            try:
                User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                print(request.POST["password1"])
                print(User.username)
                User.save()
                return HttpResponse("User created successfully")
            except:
                return HttpResponse("Username already exists")
        return HttpResponse("Password do not match")


def home(request):
    return render(request, "./home.html")


def checkPassword(password1: str, password2: str) -> bool:
    if password1 == password2:
        return True
    return False
