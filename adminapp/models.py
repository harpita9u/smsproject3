from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title
from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.Register_Number
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phnno = models.CharField(max_length=20)
    email = models.EmailField()
    feedback = models.TextField(max_length=150)

    def __str__(self):
        return f'Feedback from {self.name}'
