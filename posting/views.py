from django.shortcuts import render
from django.views import View
from posting.services import PostingService

# Create your views here.
class IndexTimelineView(View):
    def get(self, request, *args, **kwargs):
        context = { 'postings_list': PostingService.find_all() }
        return render(request, 'index.html', context)