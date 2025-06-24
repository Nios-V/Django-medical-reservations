from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import CustomUser

# Create your tests here.


class RegisterTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('register')
        self.valid_payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'role': 'doctor'
        }

    def test_user_registration_success(self):
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.first().username,
                         self.valid_payload['username'])

    def test_user_registration_missing_fields(self):
        payload = self.valid_payload.copy()
        del payload['password']
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
