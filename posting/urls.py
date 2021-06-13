from django.urls import path
from posting.views import PostingAddView, PostingEditView, PostingDetailView, PostingDeleteView, CommentAddView

app_name = 'posting'

urlpatterns = [
    path('new/', PostingAddView.as_view(), name='add'),
    path('<int:pk>', PostingDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', PostingEditView.as_view(), name='edit'),
    path('delete/<int:pk>', PostingDeleteView.as_view(), name='delete'),
    path('comment/<int:posting_pk>', CommentAddView.as_view(), name='comment'),
]