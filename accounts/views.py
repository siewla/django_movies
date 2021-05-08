from accounts.serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import *
from rest_framework import exceptions
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from movies.models import Movie

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"message": "user is registered"})
        else:
            return Response({"message": "user is not registered"})


@api_view(['POST'])
@permission_classes([AllowAny])
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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def private_view(request):
    # return Response({"message" : "Ah you see me!"})
    
    if request.method == "POST":
        movie_id = request.data.get("movie")

        if movie_id is None:
            raise exceptions.ValidationError({"detail":"no movie was sent"})
        
        # fav = FavouriteSerializer(data={"movie":movie_id, "user":request.user.id})

        # if fav.is_valid():
        #     fav.save()
        #     return Response({"message" : "Fav Movie is added to user"})

        try:
            m = Movie.objects.get(pk=movie_id)
            Favourite.objects.create(movie=m, user=request.user)
            return Response({"message" : "Fav Movie is added to user"})
        except ValidationError:
            raise exceptions.ValidationError({"detail":"movie not found or created"})


        
    elif request.method == "GET":
        user = get_user_model().objects.get(pk=request.user.id)
        u = UserSerializer(instance=user).data
        del u['password']

        return Response(u)