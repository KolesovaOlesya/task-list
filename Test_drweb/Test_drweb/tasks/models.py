from django.db import models

# Create your models here.


class Status(models.Model):
    status = models.TextField(max_length=140)

    def __str__(self):
        return self.status


class Task(models.Model):
    create_time = models.DateTimeField('date create', auto_now_add=True)
    start_time = models.DateTimeField('date start', blank=True, null=True)
    exec_time = models.CharField('date exec', max_length=100, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
