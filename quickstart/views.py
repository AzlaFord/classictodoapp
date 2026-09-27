from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from quickstart.serializers import GroupSerializer, UserSerializer, TasksSerailizer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by("date")
    serializer_class = TasksSerailizer

    def create(self, request, pk=):
        task = Tasks.objects.create(description=pk)
        task.save()
        return Response({"status":"task added ?"})

        