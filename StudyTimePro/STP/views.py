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
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
         user = form.save()
         if user is not None:
            login(self.request, user)
         return super(RegisterPage,self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('talks')
        return super(RegisterPage, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['form'])  # Añade esta línea para imprimir el contenido del formulario
        return context


#lista de tareas
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context ['tasks'].filter(user=self.request.user)
        context['count'] = context ['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'STP/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','created','due_date','priority','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','created','due_date','priority','complete']
    success_url = reverse_lazy('tasks')
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


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR,"templates")'
)

def index(request):
    return render(request, "STP/index.html")

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