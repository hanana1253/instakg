from django.contrib.auth.models import User
from django.contrib import auth

from authentication.models import Profile
from authentication.dto import EditDto, SignupDto, LoginDto

from social.models import Relationship
from utils import build_error_data, build_success_data

class UserService():
    @staticmethod
    def signup(dto: SignupDto):
        if not (dto.userid and dto.userpw and dto.userpw_check and dto.name):
            return build_error_data('MISSING_INPUT')

        if len(User.objects.filter(username=dto.userid)) > 0:
            return build_error_data('TAKEN_ID')

        if dto.userpw != dto.userpw_check:
            return build_error_data['INVALID_PW']

        user = User.objects.create_user(username=dto.userid, password=dto.userpw)
        profile = Profile.objects.create(user=user, name=dto.name)
        relationship = Relationship.objects.create(profile=profile)
        relationship.followers.add(profile)
        return build_success_data(user)

    @staticmethod
    def login(dto: LoginDto):
        if not (dto.userid and dto.userpw):
            return build_error_data('MISSING_INPUT')
        
        if len(User.objects.filter(username=dto.userid)) == 0:
            return build_error_data('INVALID_ID')
        
        auth_user =  auth.authenticate(username=dto.userid, password=dto.userpw)
        if not auth_user:
            return build_error_data('INVALID_PW')
        
        return build_success_data(auth_user)
    
    @staticmethod
    def edit(dto: EditDto):
        my_profile = Profile.objects.filter(pk=dto.my_pk)
        my_profile.update(
            introduction=dto.introduction
        )
        return build_success_data(my_profile)