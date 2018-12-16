from rest_framework.permissions import BasePermission

from Test_drweb.tasks.models import Task


class CanRun(BasePermission):
    def has_object_permission(self, request, view, obj):
        tasks_run_count = Task.objects.filter(status=2).count()
        print(tasks_run_count)
        if tasks_run_count > 2:
            return False
        else:
            return True
