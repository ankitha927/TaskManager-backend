from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']

    def validate_due_date(self, value):
        if not value:
            raise serializers.ValidationError("Due date is required")
        return value