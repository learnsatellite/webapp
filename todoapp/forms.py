from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import Task, User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        required = False,
        choices = [('', '')] + Task.CHOICES + [('all', 'ALL')] 
    )

class DateInput(forms.DateInput):
    input_type = "date"

class TaskForm(ModelForm):
    class Meta:
        model = Task
        # ここで、form_as.pで表示される入力フォーム
        fields = ["title", "description", "status", "duedate"]
        widgets = {
            "duedate": DateInput(),
            "status": forms.Select(attrs = {"required": True})
        }
        labels = {
            "title" : "タスク名",
            "description" : "詳細",
            "status" : "ステータス",
            "duedate": "期日"
        }
    
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")


        if not status:
            self.add_error("status", "リスト内の項目を選択してください。")