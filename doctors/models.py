from django.db import models
from django.conf import settings
from specialities.models import Speciality

# Create your models here.


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile'
    )

    speciality = models.ForeignKey(
        Speciality, on_delete=models.SET_NULL, null=True)
    license_number = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Dr. {self.user.username} - {self.speciality.name if self.speciality else 'No Speciality'}"
