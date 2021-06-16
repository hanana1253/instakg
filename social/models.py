from django.db import models
from authentication.models import Profile
# Create your models here.

class Relationship(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='relationship')
    followers = models.ManyToManyField(Profile, related_name='target_relationship', blank=True)

