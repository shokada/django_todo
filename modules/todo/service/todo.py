from modules.todo.models.todo import Todo


def create(**params):
    return Todo.create(**params)


def get_all():
    return Todo.get_list_all()


def get_by_id(id):
    return Todo.get_by_id(id)


def get_done_todo_list():
    return Todo.get_done_todo_list
