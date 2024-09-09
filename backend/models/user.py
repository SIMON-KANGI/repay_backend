from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    profile= models.URLField(default="Unknown")
    location= models.CharField(max_length=255, default="unknown", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone= models.IntegerField()
    is_active = models.BooleanField(default=True)
    role=models.CharField(max_length=20)
    account_type=models.CharField(max_length=20)
    
    