from django.urls import path 
from apps.users.api import api

urlpatterns = [
    path('users/',api.user_api_view,name='users'),
    path('users/<int:pk>',api.user_detail_api_view,name='users_detail')
]