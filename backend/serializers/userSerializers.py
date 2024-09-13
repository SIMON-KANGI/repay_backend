
from backend.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from backend.models.finance import Account
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'location', 'phone','role', 'account_type', 'profile', 'is_active', 'is_superuser', 'is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Password hashing is done automatically by Django
            location=validated_data.get('location', 'unknown'),  # Use .get() for optional fields
            phone=validated_data.get('phone', None),
            account_type=validated_data.get('account_type', 'standard'),
            role=validated_data.get('role', 'standard'),  # Default role if not provided
            profile=validated_data.get('profile', 'Unknown')  # Default profile if not provided
        )
        return user
# serializers.py


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)  # Use email for login

    class Meta:
        model = User
        fields = ('email', 'password')  # Only include email and password

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        # Find the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "No user with this email exists."})

        # Check if the password matches
        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Incorrect password."})

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError({"detail": "This account is inactive."})

        # Call the parent class validate method with the correct fields
        data = super().validate({
            'username': user.username,  # Pass username for token generation
            'password': password
        })
        print('data:', data)
        return data

