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

    def test():
        return 1 + 11

    def test1():
        return 2 + 2

    def test2():
        return 3 + 3

    def test3():
        return 3 + 3

    def test4():
        return 3 + 4

    def test5():
        return 3 + 4

    def test6():
        return 3 + 5
