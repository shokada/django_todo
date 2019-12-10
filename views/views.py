from django.shortcuts import render
from modules.todo import service as todo_sv


def todo_list(request):
    all_todo = todo_sv.get_all()
    return render(request, "./todo/index.html", {})
