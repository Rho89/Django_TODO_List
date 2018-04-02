from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=250, unique=True)
    user = models

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
    
    class Admin:
        pass


PRIORITY_CHOICES = (
    (1, 'Low'),
    (2, 'Normal'),
    (3, 'High'),
)


class Todo(models.Model):
    title = models.CharField(max_length=250, default="Todo " + str(id))
    created_date = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)
#    todo_list = models.ForeignKey(List, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']

    class Admin:
        pass

