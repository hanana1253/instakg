from django.shortcuts import render, redirect
from django.views import View, generic
from posting.models import Posting
from posting.services import PostingService, CommentService
from posting.dto import PostingDto, UpdateDto, CommentDto
import time
from utils import get_time_passed


# Create your views here.
class IndexTimelineView(View):
    def get(self, request, *args, **kwargs):
        context = { 'postings_list': PostingService.find_all(), 'now': -time.time() }
        print('', (float(time.time())-float(context['postings_list'].first().created_at))//(60*60), '시간 경과')
        return render(request, 'index.html', context)

class PostingDetailView(generic.DetailView):
    template_name = 'posting_detail.html'
    model = Posting
    context_object_name = 'posting'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['since_created'] = get_time_passed(context['posting'])
        return context

class PostingAddView(View):
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
            content=request.POST['content']   
        )

class PostingEditView(View):
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

class PostingDeleteView(View):
    def post(self, request, *args, **kwargs):
        target_posting_pk = kwargs['pk']
        PostingService.delete(target_posting_pk)
        return redirect('index')

class CommentAddView(View):
    def post(self, request, *args, **kwargs):
        comment_dto = self._build_comment_dto(request)
        CommentService.create(comment_dto)
        return redirect('index')

    def _build_comment_dto(self, request):
        return CommentDto(
            posting_pk=self.kwargs['posting_pk'],
            writer=request.user.profile,
            content=request.POST['content']
        )

