from django.contrib import admin
from authentication.models import Profile
from posting.models import Posting, Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Posting)
admin.site.register(Comment)