from django.test import TestCase

from modules.todo import service as todo_sv
from modules.todo.models.todo import Todo


class TodoServiceTests(TestCase):

    def test_create(self):
        todo_sv.create(text='hoge', is_done=False)
        todo_list = Todo.objects.all()
        self.assertEqual(len(todo_list), 1)
