from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', register_view, name='register'),
]