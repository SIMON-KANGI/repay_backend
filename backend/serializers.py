# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','location', 'phone', 'account_type', 'profile']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],# Password hashing is done automatically
            location=validated_data['location'],
            phone=validated_data['phone'],
            account_type=validated_data['account_type'],
            profile=validated_data['profile'] # Default profile URL is set here. Can be updated as per requirement.
        )
        return user
