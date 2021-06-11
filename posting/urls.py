from django.urls import path
from posting.views import PostingAddView, PostingEditView, PostingDetailView, CommentAddView

app_name = 'posting'

urlpatterns = [
    path('new/', PostingAddView.as_view(), name='add'),
    path('edit/<int:pk>', PostingEditView.as_view(), name='edit'),
    path('<int:pk>', PostingDetailView.as_view(), name='detail'),
    path('comment/<int:posting_pk>', CommentAddView.as_view(), name='comment'),
]