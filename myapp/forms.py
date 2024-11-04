from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)
    description = forms.CharField(label="Descripción", widget=forms.Textarea)
    project = forms.IntegerField(label="Proyecto")


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
