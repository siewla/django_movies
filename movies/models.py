from django.db import models
import uuid 
# Create your models here.

class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False
    )
    name=models.CharField(max_length=200, null=False)
    year=models.IntegerField(null=False)
    poster=models.CharField(max_length=200, null=False)
