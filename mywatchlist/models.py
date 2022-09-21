from operator import mod
from django.db import models

# Create your models here.
class MywatchlistItem(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=100)
    review = models.TextField()