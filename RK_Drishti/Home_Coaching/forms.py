# forms.py
from django import forms
from .models import Note
from .models import Course

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'file']

class CourseFrom(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'content', 'file']