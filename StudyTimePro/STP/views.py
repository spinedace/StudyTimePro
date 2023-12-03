from typing import Any
from django.shortcuts import render ,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from django.views.generic.edit import CreateView

from django.views.generic import ListView
from django.views.generic import DetailView

from django.views import View
from django.http import JsonResponse

from django.utils import timezone

import datetime 
import calendar as cal

from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from django import forms
from .forms import CustomUserCreationForm


# Create your views here.

#login/register

class CustomLoginView(LoginView):
    template_name = 'STP/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy ('tasks')

class RegisterPage(FormView):
    template_name = 'STP/register.html'
    form_class = CustomUserCreationForm  # Cambia a tu nuevo formulario personalizado
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['form'])
        return context


#lista de tareas
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'STP/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context ['tasks'].filter(user=self.request.user)
        context['count'] = context ['tasks'].filter(complete=False).count()
        # Filtra tareas vencidas
        context['tasks_overdue'] = context ['tasks'].filter(complete=False, due_date__lt=timezone.now())
        context['count_overdue'] = context ['tasks'].filter(complete=False, due_date__lt=timezone.now()).count()

        # Filtra tareas actuales
        context['tasks_current'] = context ['tasks'].filter(complete=False, due_date__gte=timezone.now())
        context['count_current'] = context ['tasks'].filter(complete=False, due_date__gte=timezone.now()).count()

        # Filtra tareas completadas
        context['tasks_completed'] = context ['tasks'].filter(complete=True)
        context['count_completed'] = context ['tasks_completed'].filter(complete=True,).count()
        return context

    


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'STP/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'created', 'due_date', 'priority']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.due_date = self.request.POST.get('due_date')  # Recupera el valor del campo oculto
        return super(TaskCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(TaskCreate, self).get_form(form_class)
        form.fields['created'].widget = forms.DateTimeInput(attrs={'class': 'form-control flatpickr'})
        form.fields['due_date'].widget = forms.DateTimeInput(attrs={'class': 'form-control flatpickr'})
        return form

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'created', 'due_date', 'priority']
    success_url = reverse_lazy('tasks')

    def get_form(self, form_class=None):
        form = super(TaskUpdate, self).get_form(form_class)
        form.fields['created'].widget = forms.DateTimeInput(attrs={'class': 'form-control flatpickr'})
        form.fields['due_date'].widget = forms.DateTimeInput(attrs={'class': 'form-control flatpickr'})
        return form
class TaskToggleCompleteView(View):
    def post(self, request, task_id):
        # Obtén la tarea
        task = Task.objects.get(id=task_id)

        # Cambia el estado de completitud
        task.complete = not task.complete
        task.save()

        # Devuelve una respuesta JSON
        return redirect('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


#calendar


class GetTasksAsJSON(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)
        task_data = []

        for task in tasks:
            task_data.append({
                'id': task.id,
                'title': task.title,
                'start': task.created.isoformat() if task.created else None,
                'end': task.due_date.isoformat() if task.due_date else None,
                'priority': task.priority,
            })

        return JsonResponse(task_data, safe=False)




class CalendarView(LoginRequiredMixin, View):
    template_name = 'STP/calendar_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar datos adicionales al contexto según sea necesario
        return context

#perfil
class UserDetailView(LoginRequiredMixin, View):
    template_name = 'STP/user_detail.html'

    def get(self, request, *args, **kwargs):
        user_profile = self.request.user
        return render(request, self.template_name, {'user_profile': user_profile})



class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'STP/user_edit.html'
    fields = [ 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('user_detail')

    def get_object(self, queryset=None):
        return self.request.user
    


#Estadísticas


class GetInfo(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'STP/estadisticas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context ['tasks'].filter(user=self.request.user)
        context['count'] = context ['tasks'].filter(complete=False).count()
        
        # Filtra tareas vencidas
        context['tasks_overdue'] = context ['tasks'].filter(complete=False, due_date__lt=timezone.now())
        context['count_overdue'] = context ['tasks'].filter(complete=False, due_date__lt=timezone.now()).count()

        # Filtra tareas actuales
        context['tasks_current'] = context ['tasks'].filter(complete=False, due_date__gte=timezone.now())
        context['count_current'] = context ['tasks'].filter(complete=False, due_date__gte=timezone.now()).count()
        
        # Filtra tareas completadas
        context['tasks_completed'] = context ['tasks'].filter(complete=True)
        context['count_completed'] = context ['tasks_completed'].filter(complete=True,).count()

        #estadisticas
        context['total']=context['count_overdue']+context['count_completed']+context['count_current']
        context['percent_overdue']=int((context['count_overdue']/context['total'])*100)
        context['percent_current']=int((context['count_current']/context['total'])*100)
        context['percent_completed']=int((context['count_completed']/context['total'])*100)


        # Contador de tareas completadas por día
        now = datetime.datetime.now()
        num_days = cal.monthrange(now.year, now.month)[1]
        num_task_for_day = [0 for _ in range(num_days)]

        for task in context['tasks_completed']:
            if task.created.month == now.month:
                if task.complete:
                    num_task_for_day[task.created.day - 1] += 1

        context['month'] = cal.month_name[now.month]
        context['num_task_for_day'] = num_task_for_day

        return context

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR,"templates")'
)

def home(request):
    return render(request, "STP/index.html")

def perfil(request):
    return render(request, "STP/perfil.html")

def calendar(request):
    return render(request, "STP/calendar.html")

def estadisticas(request):
    return render(request, "STP/estadisticas.html")

def ayuda(request):
    return render(request, "STP/ayuda.html")

def login2(request):
    return render(request, "STP/login2.html")

# def register(request):
#     return render(request, "STP/register.html")