Django version 4.2.7

django_vue_todo で

```
pipenv shell
```

した状態で

```
python manage.py runserver
```

簡単な内容<br>
クラス的なもの → task/views.py など<br>
ここから開くビューと値を渡す<br>
同じ task で使う form も forms.py で記載<br>
Django では、基本的に{% csrf_token %}を定義していないと、データを変更できない
