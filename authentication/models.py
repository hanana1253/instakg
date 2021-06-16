from django.db import models
from django.contrib.auth.models import User
from behaviors import BaseFields

# Create your models here.
class Profile(BaseFields):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=8)
    introduction = models.TextField(null=True, blank=True)
    profile_img = models.ImageField(upload_to='profile_pic', default='profile_pic/close-button-png-30230.png', null=True, blank=True)