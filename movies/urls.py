from django.urls import path
from movies.views import *

urlpatterns = [
    path('', index_view, name='all_movies'),
]