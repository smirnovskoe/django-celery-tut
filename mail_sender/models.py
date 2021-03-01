from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return self.name


class TestModel(models.Model):
    ...
