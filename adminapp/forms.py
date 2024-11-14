from django import forms
from .models import Task
from .forms import *

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentList
        fields=['Register_Number','Name']
class UploadFileForm(forms.Form):
    file = forms.FileField()
from django import forms
from .models import Feedback  # Assuming you have a Feedback model

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phnno', 'email', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phnno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'maxlength': 150, 'placeholder': 'Your feedback (max 150 characters)'}),
        }
        labels = {
            'name': 'Full Name',
            'phnno': 'phone Number',
            'email': 'Email Address',
            'feedback': 'Feedback',
        }
