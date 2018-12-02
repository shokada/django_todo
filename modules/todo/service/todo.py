from modules.todo.models.todo import Todo


def create(**params):
    return Todo.create(**params)


def get_all():
    return Todo.get_list_all()
