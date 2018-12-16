import time
import random
from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from Test_drweb.tasks.models import Task, Status
from Test_drweb.tasks.permissions import CanRun
from Test_drweb.tasks.serializers import TaskSerializer, CreateTaskSerializer, StatusSerializer


class TasksListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(detail=True, permission_classes=[CanRun], methods=['put'])
    def run(self, request, pk=None):
        task = self.get_object()
        task.start_time = timezone.now()
        task.status = Status.objects.get(id=2)
        task.save()
        time.sleep(random.randint(0, 10))
        task.status = Status.objects.get(id=3)
        task.exec_time = str(timezone.now() - task.start_time)
        task.save()
        return Response(self.get_serializer(instance=task).data)


class CreateTaskViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateTaskSerializer
    queryset = Task.objects.all()


class StatusViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = StatusSerializer
    queryset = Task.objects.all()
