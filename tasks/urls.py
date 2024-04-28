from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/v1/", include_docs_urls(title="task_api")),
    path("signup/", views.signUp, name="signup"),
    path("home/", views.home, name="home"),
]
