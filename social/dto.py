from dataclasses import dataclass
from authentication.models import Profile

@dataclass
class FollowDto():
    target_pk: int
    my_profile: Profile