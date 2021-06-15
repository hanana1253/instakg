from posting.dto import PostingDto, UpdateDto, CommentDto, LikeDto
from authentication.models import Profile
from posting.models import Posting, Comment
import time

class PostingService():

    @staticmethod
    def find_all():
        postings = Posting.objects.filter(is_deleted=False).order_by('-created_at')
        return postings

    @staticmethod
    def find_by_pk(pk):
        return Posting.objects.filter(pk=pk).first()

    @staticmethod
    def add(dto: PostingDto):
        post = Posting.objects.create(author=dto.author, photo=dto.photo, content=dto.content)
        return {'error':{'state': False }, 'data': post}

    @staticmethod
    def update(dto: UpdateDto):
        post = Posting.objects.filter(pk=dto.posting_pk).update(content=dto.content, updated_at=time.time())
        return {'error': {'state': False }, 'data': post}
    
    @staticmethod
    def delete(pk):
        Posting.objects.filter(pk=pk).update(is_deleted=True)
        return {'error': {'state': False }}
    @staticmethod
    def like(dto: LikeDto):
        target_posting = Posting.objects.filter(pk=dto.target_pk).first()
        if dto.my_profile not in target_posting.like_users.all():
            target_posting.like_users.add(dto.my_profile)
        else:
            target_posting.like_users.remove(dto.my_profile)
        return {'error': {'state': False }}


class CommentService():
    @staticmethod
    def create(dto: CommentDto):
        target_posting = Posting.objects.filter(pk=dto.posting_pk).first()
        comment = Comment.objects.create(
            writer=dto.writer,
            post=target_posting,
            content=dto.content
        )
        return {'error': {'state': False }, 'data': comment }

    @staticmethod
    def like(dto: LikeDto):
        target_comment = Comment.objects.filter(pk=dto.target_pk).first()
        if dto.my_profile not in target_comment.like_users.all():
            target_comment.like_users.add(dto.my_profile)
        else:
            target_comment.like_users.remove(dto.my_profile)
        return {'error': {'state': False }}
