from django.shortcuts import render, redirect
from django.views import generic, View
from authentication.models import Profile
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
        pass

    def post(self, request, *args, **kwargs):
        pass

class LoginView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

def logout(request):
    auth.logout(request)
    return redirect('index')