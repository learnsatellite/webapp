from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import Task, User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All')] + Task.CHOICES
    )

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        # ここで、form_as.pで表示される入力フォーム
        fields = ["title", "description", "completed", "status", "duedate"]
        widgets = {
            "duedate": DateInput(),
        }