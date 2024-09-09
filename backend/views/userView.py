from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from backend.serializers import UserSerializer
from backend.models.user import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes =[AllowAny]