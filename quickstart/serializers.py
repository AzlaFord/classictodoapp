from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Tasks


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class TasksSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ["url","description","status","date"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]