from accounts.models import CustomUser
from accounts.serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework import permissions



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    serializer_class = RegistrationSerializer


