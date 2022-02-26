from rest_framework import serializers
from accounts.models import CustomUser,Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'profession', 'description', 'date_of_join', 'gender', 'profile_image' ]

class UserListSerializer(serializers.ModelSerializer):
    
    profile = UserProfileSerializer(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'password2' 'date_of_birth','is_staff', 'is_active','profile']

    def create(self, validated_data):
        print("validate data: ", validated_data)
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']
        date_of_birth = validated_data['date_of_birth']
        full_name = validated_data['full_name']
        description = validated_data['description']
        profession = validated_data['profession']
        gender = validated_data['gender']
        profile_image = validated_data['profile_image']
        user = CustomUser.objects.create(email=email, date_of_birth=date_of_birth)
        if password != password2:
            raise ValueError("Password Does not Match")
        user.set_password(password)
        user.save()
        user.user_profile.full_name = full_name
        user.user_profile.description = description
        user.user_profile.profession = profession
        user.user_profile.gender = gender
        user.user_profile.profile_image = profile_image
        user.user_profile.save()
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    profile= UserProfileSerializer()
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'date_of_birth','password', 'password2','profile']