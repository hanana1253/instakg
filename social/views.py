from django.http.response import JsonResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from .dto import FollowDto
from social.services import FollowService
# Create your views here.

class FollowView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'
    def post(self, request, *args, **kwargs):
        follow_dto = self._build_follow_dto(request)
        follow_data = FollowService.toggle(follow_dto)
        return JsonResponse(follow_data)

    def _build_follow_dto(self, request):
        return FollowDto(
            target_pk=self.kwargs['pk'],
            my_profile=request.user.profile
        )

    