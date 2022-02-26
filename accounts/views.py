from django.shortcuts import render
from accounts.models import CustomUser
from accounts.serializers import UserListSerializer, RegistrationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import get_user_model


class UserAPIView(generics.ListCreateAPIView):
    #queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    serializer_class = UserListSerializer

    def post(self, request, format=None):
        serializar = self.serializer_class(data=request.POST)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)
        return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer