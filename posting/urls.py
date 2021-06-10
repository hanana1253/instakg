from django.urls import path
from posting.views import IndexPostingsListView

urlpatterns = [
    path('', IndexPostingsListView.as_view(), name='index'),
]