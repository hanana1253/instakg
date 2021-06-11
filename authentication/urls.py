from django.urls import path, include
from authentication.views import ProfileDetailView, ProfileEditView, SignupView, LoginView, logout

app_name = 'user'

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]