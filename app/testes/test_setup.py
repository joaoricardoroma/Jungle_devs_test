from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from app.models import Author


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'username': "email123",
            'password': "email@email.com",
        }

        User.objects.create(username=self.user_data["username"], password=self.user_data["password"])
        Author.objects.create(name="jHON GREEN"),
        import ipdb;ipdb.set_trace()
        self.login_response = self.client.post(self.login_url, self.user_data, format="json")
        self.article_list = reverse("article-list")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

