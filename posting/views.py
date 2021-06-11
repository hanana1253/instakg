from django.shortcuts import render, redirect
from django.views import View, generic
from posting.models import Posting
from posting.services import PostingService
from posting.dto import PostingDto

# Create your views here.
class IndexTimelineView(View):
    def get(self, request, *args, **kwargs):
        context = { 'postings_list': PostingService.find_all() }
        return render(request, 'index.html', context)

class PostingDetailView(generic.DetailView):
    template_name = 'posting_detail.html'
    model = Posting
    context_object_name = 'posting'

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
        pass

    def post(self, request, *args, **kwargs):
        pass

class CommentAddView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass