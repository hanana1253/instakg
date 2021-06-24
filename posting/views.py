import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin

from posting.models import Posting
from posting.services import PostingService, CommentService
from posting.dto import LikeDto, PostingDto, UpdateDto, CommentDto
import time
from utils import get_time_passed


# Create your views here.
class IndexTimelineView(View):

    def get(self, request, *args, **kwargs):
        try:
            postings_list = PostingService.find_all(request.user.profile)
        except:
            postings_list = None
        context = { 'postings_list': postings_list, 'now': -time.time() }
        return render(request, 'index.html', context)

class PostingDetailView(LoginRequiredMixin, generic.DetailView):
    redirect_field_name = None
    login_url = '/user/login/'
    template_name = 'posting_detail.html'
    model = Posting
    context_object_name = 'posting'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['since_created'] = get_time_passed(context['posting'])
        return context

class PostingAddView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'
    def get(self, request, *args, **kwargs):
        return render(request, 'add.html')

    def post(self, request, *args, **kwargs):
        posting_dto = self._build_add_dto(request)
        result = PostingService.add(posting_dto)
        if result['error']['state']:
            return redirect('index')
        return redirect('index')
    
    @staticmethod
    def _build_add_dto(request):
        return PostingDto(
            author=request.user.profile,
            photo=request.FILES['photo'],
            content=request.POST['content'],
        )

class PostingEditView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'

    def get(self, request, *args, **kwargs):
        target_posting = PostingService.find_by_pk(kwargs['pk'])
        context = {'posting': target_posting}
        return render(request, 'edit.html', context)

    def post(self, request, *args, **kwargs):
        update_dto = self._build_update_dto(request.POST)
        PostingService.update(update_dto)
        return redirect('posting:detail', kwargs['pk'])

    def _build_update_dto(self, post_data):
        return UpdateDto(
            posting_pk=self.kwargs['pk'],
            content=post_data['content']
        )

class PostingDeleteView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'

    def post(self, request, *args, **kwargs):
        target_posting_pk = kwargs['pk']
        PostingService.delete(target_posting_pk)
        return redirect('index')

class PostingLikeView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'

    def post(self, request, *args, **kwargs):
        like_dto = self._build_like_dto(request)
        like_data = PostingService.like(like_dto)
        print(json.loads(request.body)['msg'])
        return JsonResponse(like_data)

    def _build_like_dto(self, request):
        return LikeDto(
            target_pk=self.kwargs['posting_pk'],
            my_profile=request.user.profile,
        )

class CommentAddView(LoginRequiredMixin, View):
    redirect_field_name = None
    login_url = '/user/login/'
    def post(self, request, *args, **kwargs):
        comment_dto = self._build_comment_dto(request)
        comment_data = CommentService.create(comment_dto)
        print(comment_data)
        print(json.loads(request.body))
        return JsonResponse(comment_data)

    def _build_comment_dto(self, request):
        return CommentDto(
            posting_pk=self.kwargs['posting_pk'],
            writer=request.user.profile,
            content=json.loads(request.body)['new_comment']
        )

class CommentLikeView(View):
    def post(self, request, *args, **kwargs):
        like_dto = self._build_like_dto(request)
        CommentService.like(like_dto)
        print(' Did it work?')
        return JsonResponse({'message': 'hello'})

    def _build_like_dto(self, request):
        return LikeDto(
            target_pk=self.kwargs['comment_pk'],
            my_profile=request.user.profile,
        )