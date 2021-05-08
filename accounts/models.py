from django.db import models
import uuid 
from movies.models import Movie
from django.contrib.auth.models import User

# Create your models here.
class Favourite(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False
    )
    user = models.ForeignKey(User, related_name="user_favourites", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="movie_favourites", on_delete=models.CASCADE)

