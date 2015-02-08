from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header

from itsdangerous import TimedJSONWebSignatureSerializer
from itsdangerous import BadSignature
from itsdangerous import SignatureExpired


class JSONWebTokenAuthentication(BaseAuthentication):
    WWW_AUTHENTICATE_REALS = getattr(settings, "JWTA_WWW_AUTHENTICATE_REALS", "api")
    AUTH_HEADER_PREFIX = getattr(settings, "JWTA_AUTH_HEADER_PREFIX", "jwt")

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return "JWT realm=\"{}\"".format(self.WWW_AUTHENTICATE_REALS)


    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or smart_text(auth[0].lower()) != self.AUTH_HEADER_PREFIX.lower():
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(_("Invalid Authorization header. "
                                                    "No credentials provided."))

        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed(_("Invalid Authorization header. "
                                                    "Credentials string should not "
                                                    "contain spaces."))

        s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
        try:
            payload = s.loads(auth[1])
        except SignatureExpired:
            raise exceptions.AuthenticationFailed(_("Signature has expired."))
        except BadSignature:
            raise exceptions.AuthenticationFailed(_("Error decoding signature."))

        user = self.authenticate_credentials(payload)

        return (user, auth[1])

    def authenticate_credentials(self, payload):
        user_model = get_user_model()
        try:
            user_id = payload["id"]

            if user_id is not None:
                user = user_model.objects.get(pk=user_id, is_active=True)
            else:
                raise exceptions.AuthenticationFailed(_("Invalid payload"))
        except user_model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid signature"))

        return user
