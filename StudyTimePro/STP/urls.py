from django.urls import path
from django.contrib import admin
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage,TaskToggleCompleteView,GetTasksAsJSON,GetInfo
from django.contrib.auth.views import LogoutView
from .views import CalendarView

from .views import UserDetailView, UserUpdateView


from django import views
from . import views

from django.contrib import admin

urlpatterns =[
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),

    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),

    path('task-toggle-complete/<int:task_id>/', TaskToggleCompleteView.as_view(), name='task-toggle-complete'),

    

    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('user/edit/', UserUpdateView.as_view(), name='user_edit'),

    # Rutas para la funcionalidad de calendario

    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('api/tasks/', GetTasksAsJSON.as_view(), name='get_tasks_as_json'),
    

    # Rutas auxiliares
    path('', views.home, name="home"),
    path('perfil', views.perfil, name="perfil"),
    path('calendar', views.calendar, name="calendar"),
    path('estadisticas', GetInfo.as_view(), name="estadisticas"),
    path('ayuda', views.ayuda, name="ayuda"),
    

    ]
