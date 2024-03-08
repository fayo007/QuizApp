from django import forms
from main.models import Quiz
from ckeditor.widgets import CKEditorWidget


class QuizCreateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="data")

    class Meta:
        model = Quiz
        fields = ['title']
        labels = {
            "title": "Nomi",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        