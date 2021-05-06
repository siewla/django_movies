from movies.serializers import MovieSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from movies.models import *
from movies.serializers import *

# Create your views here.
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def index_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer= MovieSerializer(movies, many=True)
    elif request.method == 'POST':
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response({'message': 'movie is saved!'})
    
    return Response(serializer.data)