from http import client
from urllib import response
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data = {
            "username": "testcase",
            "email":  "testcase@example.com",
            "password" :  "newpassword123",
            "password2" :  "newpassword123",
        }
        response = self.client.post(reverse('registration'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username= "example", password= "example123")
        
        
        
        
    def test_login(self):
        
        data = {
            
            "username": "example",
            "password": "example123",
        }
       

        response = self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


