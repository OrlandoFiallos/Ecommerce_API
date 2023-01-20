from django.urls import path 
from apps.users.api import api

urlpatterns = [
    path('users/',api.user_api_view,name='users')
]