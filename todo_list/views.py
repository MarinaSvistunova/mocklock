from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from todo_list.models import TaskToDo

from todo_list.forms import SaveTask


def main_page(request):
    context = {}
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        tasks = TaskToDo.objects.filter(user=user)

        context['tasks'] = tasks.filter(done=False)
        context['tasks_done'] = tasks.filter(done=True)

        return render(request, 'todo_list/index.html', context)
    else:
        return redirect('login_view')


def update_task(request, id):
    if request.user.is_authenticated:
        task = TaskToDo.objects.get(id=id)
        if task.done:
            task.done = False
            task.save()
        else:
            task.done = True
            task.save()
        return redirect('tasks_list')
    else:
        return redirect('login_view')


def delete_task(request, id):
    if request.user.is_authenticated:
        task = TaskToDo.objects.get(id=id)
        task.delete()
        return redirect('tasks_list')
    else:
        return redirect('login_view')


def new_task(request):
    context = {}
    if request.user.is_authenticated:
        form = SaveTask(request.POST)
        user = User.objects.get(id=request.user.id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            context['form'] = form
            return redirect('tasks_list')
        context['form'] = form
        return redirect('tasks_list')
    else:
        return redirect('login_view')


def save_task(request, id):
    context = {}
    if request.user.is_authenticated:
        task = TaskToDo.objects.get(id=id)
        form = SaveTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        return redirect('tasks_list')
    else:
        return redirect('login_view')


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'todo_list/register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'todo_list/login.html'
