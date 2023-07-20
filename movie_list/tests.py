from django.test import TestCase
from django.test.client import Client
# Create your tests here.
class HomeViewTest(TestCase):
    def test_index(self):
        client= Client()
        response = client.get('/')
        assert response.status_code == 200

