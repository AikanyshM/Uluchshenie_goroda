from rest_framework import serializers
from .models import User, Citizen, AdminUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def save(self):
        user = User(username=self.validated_data['username'],
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        read_only_fields = ['username',]

class CitizenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Citizen
        fields = "__all__"

class CitizenCreateSerializer(UserCreateSerializer):
    citizen = CitizenSerializer()

    class Meta:
        model = User
        fields = ["citizen", "username", "password", "password2", 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def save(self):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()

        citizen = Citizen(
            user=user, 
            INN=self.validated_data['citizen']['INN'],
            email=self.validated_data['citizen']['email'],
            )
        citizen.save()
        return user
