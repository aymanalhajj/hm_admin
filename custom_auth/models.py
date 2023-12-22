from django.db import models

from datetime import datetime, timedelta

import jwt
from django.conf import settings
# from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

# User = get_user_model()


from django.utils.translation import gettext_lazy as _

class UserType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('user type name'))
    def __str__(self) -> str:
        return self.name
    class Meta:
        managed = True
        verbose_name = _('User Type')
        verbose_name_plural = _('User Type')

class UserAccount(models.Model):
    first_name = models.CharField(max_length=100,verbose_name=_('first name'))
    second_name = models.CharField(max_length=100,verbose_name=_('second name'), blank=True, )
    third_name = models.CharField(max_length=100,verbose_name=_('third name'), blank=True, )
    fourth_name = models.CharField(max_length=100,verbose_name=_('fourth name'), blank=True, )
    last_name = models.CharField(max_length=100,verbose_name=_('last name')  )
    email = models.CharField(max_length=100,verbose_name=_('email'), blank=True, )
    mobile = models.CharField(max_length=100,verbose_name=_('mobile'))
    username = models.CharField(max_length=100,verbose_name=_('username'))
    password = models.CharField(max_length=100,verbose_name=_('password'))
    type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING,verbose_name=_('user type'))

    def check_password(self,pwd):
        user = UserAccount.objects.filter(username = self.username, password = pwd).first()
        return user
    def __str__(self) -> str:
        return self.first_name + '  ' + self.last_name
    class Meta:
        managed = True
        verbose_name = _('User Account')
        verbose_name_plural = _('User Account')





# class JWTAuthentication(authentication.BaseAuthentication):
class JWTAuthentication():
    @classmethod
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return {'message':'no token passed','status':'invalid'}

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)  # clean the token

        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            return {'message':'Invalid signature','status':'invalid'}
            # raise AuthenticationFailed('Invalid signature')
        except:
            return {'message':'token parse error','status':'invalid'}
            # raise ParseError()

        # Get the user from the database
        username_or_mobile = payload.get('user_identifier')
        if username_or_mobile is None:
            return {'message':'User identifier not found in JWT','status':'invalid'}
            raise AuthenticationFailed('User identifier not found in JWT')

        user = UserAccount.objects.filter(username=username_or_mobile).first()
        if user is None:
            user = UserAccount.objects.filter(mobile=username_or_mobile).first()
            if user is None:
                return {'message':'User not found in DB','status':'invalid'}
                # raise AuthenticationFailed('User not found')

        # Return the user and token payload
        from .serializer import CustomUserAccountSerializer
        serializer = CustomUserAccountSerializer(user)
        return {'status':'succeed','user_id':user.id,'user_name':user.username, "user":user}
        # return user, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'user_identifier': user.username,
            'exp': int((datetime.now() + timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            # set the expiration time for 5 hour from now
            'iat': datetime.now().timestamp(),
            'username': user.username,
            'mobile': user.mobile
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token