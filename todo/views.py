from django.shortcuts import render, redirect
from .models import Todo, Todoweekend
from .forms import AddForm, AddFormweekend
# Create your views here.


def todo_weekly(request) :
    return render(request, "todo_weeklytemplate.html")

def todo_week(request) :
    if request.method == 'POST' :
        form = AddForm(request.POST)
        if form.is_valid() :
            form.save()
    todos = Todo.objects.all()
    form = AddForm()
    data = {
        "todos" : todos,
        "form" : form,
    }
    return render(request, "todo_weektemplate.html", data)



def todo_weekend(request) :
    if request.method == 'POST' :
        form = AddFormweekend(request.POST)
        if form.is_valid() :
            form.save()
    todos = Todoweekend.objects.all()
    form = AddFormweekend()
    data = {
        "todos" : todos,
        "form" : form,
    }
    return render(request, "todo_weekendtemplate.html", data)



def delete_todo(request, pk) :
    target = Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todosweek")

def todo_done(request, pk) :
    target = Todo.objects.get(pk=pk)
    target.is_done = True
    target.save()
    return redirect("todosweek")



def delete_todoweekend(request, pk) :
    target = Todoweekend.objects.get(pk=pk)
    target.delete()
    return redirect("todosweekend")

def todo_doneweekend(request, pk) :
    target = Todoweekend.objects.get(pk=pk)
    target.weekendis_done = True
    target.save()
    return redirect("todosweekend")





#def todo_homeviews(request) :
#    return render(request, "todo_hometemplate.html")

#def todo_dateviews(request) :
#    if request.method == 'POST' :
#        form = AddForm(request.POST)
#        if form.is_valid() :
#            form.save()
#    todos = Todo.objects.all()
#    form = AddForm()
#    data = {
#        "todos" : todos,
#        "form" : form,
#    }
#    return render(request, "todo_datetemplate.html", data)