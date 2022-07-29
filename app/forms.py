from socket import fromshare
from django import forms
from app.models import *
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'