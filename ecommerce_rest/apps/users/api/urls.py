from django.urls import path 
from apps.users.api import api

urlpatterns = [
    path('users/',api.user_list,name='users'),
    path('users/<int:pk>',api.user_detail,name='users_detail')
]