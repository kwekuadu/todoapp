from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title']
        widgets = {
            
            'title' : forms.TextInput(attrs={'class':'form-control form-control-sm mb-2','placeholder':'Todo Title','autofocus':True, 'required':True})
        }

