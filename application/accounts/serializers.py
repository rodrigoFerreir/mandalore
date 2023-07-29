from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_admin'] = user.is_admin
        token['email'] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def update(self, instance: User, validated_data: dict):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email')
        instance.username = validated_data.get('username')

        if not instance.check_password(validated_data.get('password')):
            raise serializers.ValidationError({"password": "Password is not correct"})

        instance.set_password(validated_data.get('new_password'))
        instance.save()

        return instance
