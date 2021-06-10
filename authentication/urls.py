from django.urls import path, include
from authentication.views import ProfileDetailView, ProfileEditView

app_name = 'profile'

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit'),
]