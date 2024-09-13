from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication 
from backend.serializers.userSerializers import UserSerializer
from backend.models.user import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes =[AllowAny]
    authentication_classes = [TokenAuthentication]
    
    
