from rest_framework import serializers
from accounts.models import CustomUser,Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password





class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'profession', 'description', 'date_of_join', 'gender', 'profile_image' ]



class RegistrationSerializer(serializers.ModelSerializer):
    profile= UserProfileSerializer(source='user_profile')
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password],style={'input_type': 'password', 'placeholder': 'Password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', 'placeholder': 'Confirm Password'})
    class Meta:
        model = CustomUser
        fields = ['email', 'date_of_birth','password', 'password2','profile']

    def create(self, validated_data):
        print("validate data: ", validated_data)
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']
        date_of_birth = validated_data['date_of_birth']
        profile_data = validated_data.pop('user_profile')
        print("Profile Data: ", profile_data)
        if password != password2:
            raise ValueError("Password Does not Match")
        user = CustomUser.objects.create(email=email, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user