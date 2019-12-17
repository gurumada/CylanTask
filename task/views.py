from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView ,UpdateView, DeleteView
from .models import task
from .forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    model = task
    context_object_name = "tasks"
    paginate_by = 5


class TaskDetailView(DetailView):
    model = task
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = task
    form_class = TaskForm
    #fields = ["content",]
    success_url = reverse_lazy("index")

    login_url = '/login/'

    template_name = "task/task_create_form.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request, "保存に失敗しました")
        return super().form_invalid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = task    
    form_class = TaskForm
    #fields = ["content",]
    template_name = "task/task_update_form.html"

    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy("detail",kwargs={"pk": self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "更新できませんでした")
        return super().form_invalid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = task
    success_url = reverse_lazy("index")

    login_url = '/login/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"削除しました")
        return super().delete(request, *args, **kwargs)