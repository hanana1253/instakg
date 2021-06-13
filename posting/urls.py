from django.urls import path
from posting.views import PostingAddView, PostingEditView, PostingDetailView, PostingDeleteView, CommentAddView, PostingLikeView, CommentLikeView

app_name = 'posting'

urlpatterns = [
    path('new/', PostingAddView.as_view(), name='add'),
    path('<int:pk>', PostingDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', PostingEditView.as_view(), name='edit'),
    path('delete/<int:pk>', PostingDeleteView.as_view(), name='delete'),
    path('comment/<int:posting_pk>', CommentAddView.as_view(), name='comment'),
    path('like/<int:posting_pk>', PostingLikeView.as_view(), name='like'),
    path('like/<int:comment_pk>', CommentLikeView.as_view(), name='comment-like'),

]