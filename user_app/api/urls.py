from django import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_app.api.views import registration,  logout

urlpatterns = [
path('login/', obtain_auth_token, name= 'login'),
path('register/', registration , name= 'registration'),
path('logout/', logout , name= 'logout'),
]