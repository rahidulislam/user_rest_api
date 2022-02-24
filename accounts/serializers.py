from rest_framework import serializers
from accounts.models import CustomUser,Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'profession', 'description', 'date_of_join', 'gender', 'profile_image' ]

class UserListSerializer(serializers.ModelSerializer):
    #user = UserProfileSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'date_of_birth','is_staff', 'is_active']