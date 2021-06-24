from behaviors import BaseFields
from django.db import models
from behaviors import BaseFields
from authentication.models import Profile
# Create your models here.

class Posting(BaseFields):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='postings', null=True, blank=True)
    photo = models.ImageField(upload_to='posting_pics')
    content = models.TextField()
    like_users = models.ManyToManyField(Profile, related_name='liked_postings', blank=True)
    img_url = models.TextField()

class Comment(BaseFields):
    post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mycomments')
    content = models.TextField()
    like_users = models.ManyToManyField(Profile, related_name='liked_comments', blank=True)
