from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from accounts.service import create_user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        return create_user(validated_data)
