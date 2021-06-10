from django.urls import path
from social.views import FollowView
app_name='social'

urlpatterns=[
    path('follow/<int:pk>', FollowView.as_view(), name='follow'),
]