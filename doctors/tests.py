from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from specialities.models import Speciality
from accounts.models import CustomUser
from .models import DoctorProfile
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.


class DoctorProfileTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='doctoruser',
            password='docpassword',
            role='doctor',
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.speciality = Speciality.objects.create(name='Cardiology')

    def test_create_doctor_profile(self):
        payload = {
            'speciality': self.speciality.id,
            'license_number': '123456',
            'bio': 'Cardiologist with 10 years of experience.',
        }
        response = self.client.post(
            reverse('doctor_profile'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['speciality'], self.speciality.id)

    def test_get_doctor_profile(self):
        self.client.post(reverse('doctor_profile'), {
            'speciality': self.speciality.id,
            'license_number': '123456',
            'bio': 'Cardiologist with 10 years of experience.',
        }, format='json')

        response = self.client.get(reverse('doctor_profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['speciality'], self.speciality.id)
