from dataclasses import dataclass

from django.core.files.base import File
from authentication.models import Profile

@dataclass
class PostingDto():
    author: Profile
    photo: File
    content: str

@dataclass
class UpdateDto():
    posting_pk: int
    content: str
