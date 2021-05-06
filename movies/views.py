from movies.serializers import MovieSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.models import *
from movies.serializers import *

# Create your views here.
@api_view(['GET'])
def index_view(request):
    movies = Movie.objects.all()
    serializer= MovieSerializer(movies, many=True)
    return Response(serializer.data)