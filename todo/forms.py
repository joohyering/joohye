from django import forms
from .models import Todo, Todoweekend

class AddForm(forms.ModelForm) :
    class Meta :
        model = Todo
        fields = ('task',)


class AddFormweekend(forms.ModelForm) :
    class Meta :
        model = Todoweekend
        fields = ('weekendtask',)