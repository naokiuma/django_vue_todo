from django.shortcuts import redirect,render
from django.views.generic import View
from pprint import pprint #ログ出力

from .forms import TaskForm
from .models import Task

# Create your views here.


class TaskView(View):
	def get(self, request):
		params = {}
		params["task"] = Task.objects.all()
		# print(params)
		params["form"] = TaskForm()
		return render(request, "task_list.html", params)
	def post(self, request):
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("task_list")
