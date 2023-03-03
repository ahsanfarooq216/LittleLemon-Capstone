from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.contrib.auth.models import User

class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu_item = MenuItem.objects.create(title='cannelloni', price=15.95, inventory=50)
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_menu_item(self):
        data = {'title': 'Pizza', 'price': 12.99, 'inventory': 30}
        response = self.client.post(reverse('menu'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 2)