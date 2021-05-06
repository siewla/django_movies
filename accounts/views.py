from accounts.serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import *
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"message": "user is registered"})
        else:
            return Response({"message": "user is not registered"})


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        User = get_user_model()

        username = request.data.get('username')
        password = request.data.get('password')

        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed('Username or password is required')
        
        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Password is not a match')

        serialized_user = UserSerializer(user).data
        # remove password in data
        del serialized_user['password']

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serialized_user
        })


        