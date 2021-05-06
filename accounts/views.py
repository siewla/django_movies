from accounts.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def register_view(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"message": "user is registered"})
        else:
            return Response({"message": "user is not registered"})
