from django import forms

from .models import task

class TaskForm(forms.ModelForm):

    content = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))

    class Meta:
        model = task
        fields = ["content", ]