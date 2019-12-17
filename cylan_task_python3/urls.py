"""cylan_task_python3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from task.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('delete/<int:pk>',TaskDeleteView.as_view(), name="delete"),
    path('update/<int:pk>', TaskUpdateView.as_view(), name="update"),
    path('create', TaskCreateView.as_view(), name="create"),
    path('detail/<int:pk>', TaskDetailView.as_view(), name="detail"),
    path('', TaskListView.as_view(), name="index"),
    path('admin/', admin.site.urls),
]
