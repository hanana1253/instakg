from authentication.models import Profile
from .dto import FollowDto

class FollowService():
    @staticmethod
    def toggle(dto: FollowDto):
        target_profile = Profile.objects.filter(pk=dto.target_pk).first()
        my_profile = dto.my_profile

        if my_profile in target_profile.relationship.followers.all():
            target_profile.relationship.followers.remove(my_profile)
        else:
            target_profile.relationship.followers.add(my_profile)
        
        return