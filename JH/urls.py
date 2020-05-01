"""JH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo.views import delete_todo, todo_done, todo_weekly, todo_week, todo_weekend, delete_todoweekend, todo_doneweekend

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('todos/', todo_view, name="todos"),
    #path('todos/in_progress', todo_in_progress, name="todos_inprogress"),
    #path('todos/date', todo_dateviews, name="todos_date"),
    path('todos/week/<pk>/delete', delete_todo, name="todo_del"),
    path('todos/week/<pk>/done', todo_done, name="todo_isdone"),
    #path('todos/home', todo_homeviews, name="todohome"),
    path('todos', todo_weekly, name="todoweekly"),
    path('todos/week', todo_week, name="todosweek"),
    path('todos/weekend', todo_weekend, name="todosweekend"),
    path('todos/weekend/<pk>/delete', delete_todoweekend, name="todo_delweekend"),
    path('todos/weekend/<pk>/done', todo_doneweekend, name="todo_isdoneweekend")
]
