from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=255, null=None)
    is_done = models.BooleanField(default=False, null=None)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_list_all(cls):
        return list(cls.objects.all())

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_done_todo_list(cls):
        return cls.objects.filter(is_done=True)
