
from kquotes.base.api import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("password", )


from calendar import timegm
from datetime import datetime
from rest_framework_jwt.settings import api_settings


class UserAuthTokenSerializer(UserSerializer):
    auth_token = serializers.SerializerMethodField()

    def get_auth_token(self, obj):
        payload = api_settings.JWT_PAYLOAD_HANDLER(obj)

        # Include original issued at time for a brand new token,
        # to allow token refresh
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        return api_settings.JWT_ENCODE_HANDLER(payload)
