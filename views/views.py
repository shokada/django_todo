from django.shortcuts import render
from modules.todo import service as todo_sv


def todo_list(request):
    return render(request, "./todo/index.html", {})
