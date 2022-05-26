from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'email': "email@email.com",
            'username': "email123",
            'password': "email@email.com",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

