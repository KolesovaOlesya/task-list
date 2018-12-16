from rest_framework import serializers

from Test_drweb.tasks.models import Task, Status


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('status',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'create_time', 'start_time', 'exec_time')
        extra_kwargs = {'start_time': {'read_only': True}, 'exec_time': {'read_only': True}}


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',)


class StatusSerializer(serializers.ModelSerializer):
    status = StatusListSerializer(read_only=False)

    class Meta:
        model = Task
        fields = ('id', 'status', 'create_time', 'start_time', 'exec_time')
