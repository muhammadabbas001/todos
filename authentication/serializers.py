from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            "password": {"write_only": True},  # Ensure the password is write-only
        }

    def validate(self, data):
        # Check if all fields are provided
        required_fields = ['username', 'password', 'first_name', 'last_name', 'email']
        for field in required_fields:
            if field not in data or not data[field].strip():
                raise serializers.ValidationError({field: f"{field} is required and cannot be empty."})
        return data

    def create(self, validated_data):
        # Use `create_user` to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return user


class PasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("The current password is incorrect.")
        return value

    def validate(self, data):
        # Check if new_password and confirm_password match
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"new_password": "Passwords do not match."})

        # Validate new password strength
        validate_password(data['new_password'])
        return data

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
