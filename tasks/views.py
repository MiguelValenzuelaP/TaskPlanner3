from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from .models import Task
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.db import IntegrityError


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
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return render(
                    request,
                    "./signup.html",
                    {
                        "form": UserCreationForm,
                        "error": f"User created successfully",
                    },
                )

            except IntegrityError as error:
                return render(
                    request,
                    "./signup.html",
                    {
                        "form": UserCreationForm,
                        "error": f"User already exists",
                    },
                )
        return render(
            request,
            "./signup.html",
            {
                "form": UserCreationForm,
                "error": "Password do not match",
            },
        )


def home(request):
    return render(request, "./home.html")


def checkPassword(password1: str, password2: str) -> bool:
    if password1 == password2:
        return True
    return False
