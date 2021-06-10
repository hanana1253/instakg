from django.contrib import admin
from authentication.models import Profile
from posting.models import Posting, Comment
from social.models import Relationship
# Register your models here.

admin.site.register(Profile)
admin.site.register(Posting)
admin.site.register(Comment)
admin.site.register(Relationship)