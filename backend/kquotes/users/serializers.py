from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer

from kquotes.base.api import serializers

from . import models
from . import gravatar


class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        exclude = ("password", )

    def get_avatar_url(self, obj):
        return gravatar.get_gravatar_url(obj.email)


class UserInfoSerializer(UserSerializer):
    class Meta:
        model = models.User
        fields = ("id", "username", "full_name", "avatar_url")


class UserAuthTokenSerializer(UserSerializer):
    auth_token = serializers.SerializerMethodField()

    AUTH_EXPIRATION = getattr(settings, "JWTA_AUTH_EXPIRATION", 3600 * 24 * 365 * 200)

    def get_auth_token(self, obj):
        s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=self.AUTH_EXPIRATION)
        return s.dumps({'id': obj.id}).decode("ascii")
