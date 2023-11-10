from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage,TaskToggleCompleteView,GetTasksAsJSON
from django.contrib.auth.views import LogoutView
from .views import CalendarView, CalendarDetailView

urlpatterns =[
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),

    path('task-toggle-complete/<int:task_id>/', TaskToggleCompleteView.as_view(), name='task-toggle-complete'),



        # Rutas para la funcionalidad de calendario


    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/', CalendarDetailView.as_view(), name='calendar_detail'),

    path('api/tasks/', GetTasksAsJSON.as_view(), name='get_tasks_as_json'),

    ]
