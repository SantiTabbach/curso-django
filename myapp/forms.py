from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)
    description = forms.CharField(label="Descripción", widget=forms.Textarea)
