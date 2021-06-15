from django.shortcuts import render, redirect
from django.views import View
from .dto import FollowDto
from social.services import FollowService
# Create your views here.

class FollowView(View):
    def post(self, request, *args, **kwargs):
        follow_dto = self._build_follow_dto(request)
        FollowService.toggle(follow_dto)
        return redirect('user:detail', kwargs['pk'])

    def _build_follow_dto(self, request):
        return FollowDto(
            target_pk=self.kwargs['pk'],
            my_profile=request.user.profile
        )

    