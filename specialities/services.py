from .models import Speciality


def create_speciality(validated_data):
    return Speciality.objects.create(**validated_data)


def get_specialities():
    return Speciality.objects.all()
