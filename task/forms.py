from django import forms
from .models import Task

# タスクを登録するためのformクラス
# Task モデルの、title フィールドを受け取る form 
class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ["title"]
		widgets = {
			"title":forms.TextInput(attrs={"class":"form-control","placeholder":"卵を買う"})
		}