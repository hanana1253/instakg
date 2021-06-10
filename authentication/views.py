from django.shortcuts import render
from django.views import generic, View
from authentication.models import Profile
# Create your views here.

class ProfileDetailView(generic.DetailView):
    template_name = 'profile.html'
    model = Profile
    context_object_name = 'profile'
    # get_context_data 오버라이딩으로 팔로워목록 컨텍스트에 넣어주기

class ProfileEditView(View):
    def get(self, request, *args, **kwargs):
        context = {'profile': Profile.objects.filter(pk=1).first()}
        return render(request, 'profile_edit.html', context)

    def post(self, request, *args, **kwargs):
        pass