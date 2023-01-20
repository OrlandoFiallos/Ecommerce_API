from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 

# @api_view(['GET','POST'])
# def user_api_view(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         users_serializer = UserSerializer(users,many=True)
#         return Response(users_serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         users_serializer = UserSerializer(data = request.data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response(users_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(users_serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def user_detail_api_view(request,pk):
#     if request.method == 'GET':
#         user = User.objects.get(pk=pk)
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data)
#     elif request.method == 'PUT':
#         user = User.objects.get(pk=pk)
#         user_serializer = UserSerializer(user,data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer.data)
#         return Response(user_serializer.errors)
#     elif request.method == 'DELETE':
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response('Deleted user')

@api_view(['GET','POST'])
def user_list(request):
    # Lista todos los usuarios, o crea uno nuevo
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Detalle usuario
@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer =UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)