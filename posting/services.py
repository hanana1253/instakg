from authentication.models import Profile
from posting.models import Posting, Comment

class PostingService():

    @staticmethod
    def find_all():
        return Posting.objects.filter(is_deleted=False)