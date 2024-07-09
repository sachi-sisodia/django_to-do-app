from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','date','is_completed']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class':'form-check'}),
            # 'user': forms.Select(attrs={'class':'form-control'}),
        }
        