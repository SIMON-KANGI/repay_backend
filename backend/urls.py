from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.userView import UserViewSet


router= DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]