from lib2to3.pgen2 import token
from tokenize import Token
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from user_app.api.serializers import Registrationserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User




@api_view(['POST',])
def registration(request):


    if request.method == 'POST':
        serializer = Registrationserializer(data = request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['username']= account.username
            data['email'] = account.email
            data['response']= "registration successful"

            token = Token.objects.get(user= account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data, status = status.HTTP_201_CREATED)


def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response( status= status.HTTP_200_OK)
        




