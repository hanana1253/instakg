from posting.dto import PostingDto
from authentication.models import Profile
from posting.models import Posting, Comment

class PostingService():

    @staticmethod
    def find_all():
        return Posting.objects.filter(is_deleted=False)

    @staticmethod
    def add(dto: PostingDto):
        post = Posting.objects.create(author=dto.author, photo=dto.photo, content=dto.content)
        return {'error':{'state': False}, 'data': post}

