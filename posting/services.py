from posting.dto import PostingDto, UpdateDto, CommentDto, LikeDto
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from authentication.models import Profile
from posting.models import Posting, Comment
import boto3
from boto3.session import Session
from datetime import datetime
import time

class PostingService():

    @staticmethod
    def find_all(my_profile):
        postings = Posting.objects.filter(is_deleted=False).filter(author__relationship__followers__in=[my_profile]).order_by('-created_at')
        return postings

    @staticmethod
    def find_by_author(my_profile):
        postings = Posting.objects.filter(author=my_profile)
        return postings

    @staticmethod
    def find_by_pk(pk):
        return Posting.objects.filter(pk=pk).first()

    @staticmethod
    def add(dto: PostingDto):
        file = dto.photo
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )
        s3_url = 'http://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/'
        post = Posting.objects.create(
            author=dto.author, 
            photo=dto.photo, 
            content=dto.content, 
            created_at=time.time(),
            img_url=s3_url+now+file.name
            )
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
            like_count = len(target_posting.like_users.all())
            return {'count': like_count, 'button_msg': '좋아요 취소'}
        else:
            target_posting.like_users.remove(dto.my_profile)
            like_count = len(target_posting.like_users.all())
            return {'count': like_count, 'button_msg': '좋아요'}

class CommentService():
    @staticmethod
    def create(dto: CommentDto):
        target_posting = Posting.objects.filter(pk=dto.posting_pk).first()
        comment = Comment.objects.create(
            writer=dto.writer,
            post=target_posting,
            content=dto.content
        )
        return {
            'user_pk': comment.writer.pk, 
            'comment': comment.content, 
            'username': comment.writer.user.username, 
            'comment_pk': comment.pk 
            }

    @staticmethod
    def like(dto: LikeDto):
        target_comment = Comment.objects.filter(pk=dto.target_pk).first()
        if dto.my_profile not in target_comment.like_users.all():
            target_comment.like_users.add(dto.my_profile)
        else:
            target_comment.like_users.remove(dto.my_profile)
        return {'error': {'state': False } }
