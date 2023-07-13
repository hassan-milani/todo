from django.forms import ModelForm
from django import forms
from .models import Task

class Task_Create(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date']
        
        
class Task_Update(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
    
    