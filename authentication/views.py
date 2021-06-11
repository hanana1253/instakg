from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import auth

from authentication.models import Profile
from authentication.dto import SignupDto, LoginDto
from authentication.services import UserService

from social.services import FollowService
# Create your views here.

class ProfileDetailView(generic.DetailView):
    template_name = 'profile.html'
    model = Profile
    context_object_name = 'profile'

class ProfileEditView(View):
    def get(self, request, *args, **kwargs):
        context = {'profile': Profile.objects.filter(pk=1).first()}
        return render(request, 'profile_edit.html', context)

    def post(self, request, *args, **kwargs):
        pass

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        signup_dto = self._build_signup_dto(request.POST)
        result = UserService.signup(signup_dto)
        if result['error']['state']:
            return render(request, 'signup.html', result)
        auth.login(request, result['data'])
        return redirect('index')
        
        
    @staticmethod
    def _build_signup_dto(post_data):
        return SignupDto(
            userid=post_data['userid'],
            userpw=post_data['userpw'],
            userpw_check=post_data['userpw-check'],
            name=post_data['name']
        )

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        login_dto = self._build_login_dto(request.POST)
        result = UserService.login(login_dto)
        if result['error']['state']:
            return render(request, 'login.html', result)
        auth.login(request, result['data'])
        return redirect('index')

    @staticmethod
    def _build_login_dto(post_data):
        return LoginDto(
            userid=post_data['userid'],
            userpw=post_data['userpw']
        )

def logout(request):
    auth.logout(request)
    return redirect('index')