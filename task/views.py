from django.shortcuts import render
from django.views.generic import View
from pprint import pprint #ログ出力

# Create your views here.


class TaskView(View):
    def get(self, request):
        return render(request, "task_list.html", context={"name": "テスト"})