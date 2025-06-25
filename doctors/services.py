from .models import DoctorProfile


def create_doctor_profile(validated_data, user):
    return DoctorProfile.objects.create(user=user, **validated_data)


def get_doctor_profile(user):
    return getattr(user, 'doctor_profile', None)
