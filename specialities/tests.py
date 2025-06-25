from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.


class SpecialityTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            role='doctor',
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_speciality(self):
        payload = {
            'name': 'Cardiology',
            'description': 'Heart-related conditions and treatments.'
        }
        response = self.client.post(
            reverse('speciality-list-create'), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], payload['name'])

    def test_list_specialities(self):
        self.client.post(reverse('speciality-list-create'),
                         {'name': 'Dermatología', 'description': 'desc for Dermatologist'}, format='json')
        self.client.post(reverse('speciality-list-create'),
                         {'name': 'Cardiología', 'description': 'desc for Cardiologist'}, format='json')

        response = self.client.get(reverse('speciality-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
