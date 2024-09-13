from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    username=models.CharField(unique=True, max_length=255)
    profile = models.URLField(default="Unknown", max_length=1000)
    location = models.CharField(max_length=255, default="unknown", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255, blank=True, null=True)  # CharField for phone numbers
    role = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Avoid reverse accessor clashes
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Avoid reverse accessor clashes
        blank=True
    )
   
    class Meta:
        app_label = 'backend'
