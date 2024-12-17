from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'last_name', 'first_name', 'email', 'password', 'is_superuser', 'get_all_permissions'
        )

    def patch(self, validated_data):
        user = self.instance
        user.last_name = validated_data.get('last_name', user.last_name)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.email = validated_data.get('email', user.email)
        password = validated_data.get('password')

        if password:
            user.set_password(password)
        user.save()
        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password', 'password_confirmation',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Пароль должен быть не менее 8 символов."})
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Введеные пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
