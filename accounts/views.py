from django.shortcuts import render
from accounts.models import CustomUser
from accounts.serializers import UserListSerializer
from rest_framework.viewsets import ModelViewSet

class UserAPIView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer