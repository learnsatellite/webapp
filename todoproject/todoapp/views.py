from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from todoapp.models import Task
from .forms import SignUpForm, TaskFilterForm, TaskForm

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"


    # 元々ListViewが持っている"get_context_data()"という関数をオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context["form"] = TaskFilterForm(self.request.GET)

        context["tasks"] = context["tasks"].filter(user = self.request.user)

        searchInputText = self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(title__icontains = searchInputText)

        status_filter = self.request.GET.get("status")
        if status_filter:
            context['tasks'] = context['tasks'].filter(status=status_filter)

        context["search"] = searchInputText

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks") 

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"

class TaskListLoginView(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")

class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)