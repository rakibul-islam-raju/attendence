from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    present = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.student)
    