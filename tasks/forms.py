from django import forms

class TaskImportForm(forms.Form):
    csv_file = forms.FileField()
