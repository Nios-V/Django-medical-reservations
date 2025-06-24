from accounts.models import CustomUser


def create_user(validated_data):
    return CustomUser.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        role=validated_data['role'],
    )
