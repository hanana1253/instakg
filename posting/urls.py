from django.urls import path
from posting.views import PostingAddView, PostingEditView

app_name = 'posting'

urlpatterns = [
    path('new/', PostingAddView.as_view(), name='add'),
    path('edit/<int:pk>', PostingEditView.as_view(), name='edit'),
]