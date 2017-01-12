
import json
import jwt

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_text
from django.views.decorators.csrf import csrf_exempt

from . import settings, exceptions

jwt_decode = settings.JWT_DECODE_HANDLER


class JSONWebTokenAuthMixin(object):
    """
    Token based authentication using the JSON Web Token standard.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string specified in the setting
    `JWT_AUTH_HEADER_PREFIX`. For example:

        Authorization: JWT eyJhbGciOiAiSFMyNTYiLCAidHlwIj
    """
    www_authenticate_realm = 'api'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user, request.token = self.authenticate(request)
        except exceptions.AuthenticationFailed as e:
            response = HttpResponse(json.dumps({'errors': [str(e)]}),
                                    status=401,
                                    content_type='application/json')

            response['WWW-Authenticate'] = self.authenticate_header(request)

            return response

        return super(JSONWebTokenAuthMixin, self).dispatch(
            request, *args, **kwargs)

    def authenticate(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return (request.user, None)

        auth = request.META.get('HTTP_AUTHORIZATION', b'').split()

        if not auth or smart_text(auth[0].lower()) != settings.JWT_AUTH_HEADER_PREFIX.lower():
            raise exceptions.AuthenticationFailed()

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed('Invalid Authorization header. No credentials '
                                                  'provided.')
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed('Invalid Authorization header. Credentials '
                                                  'string should not contain spaces.')
        try:
            payload = jwt_decode(auth[1])
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed('Signature has expired.')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Error decoding signature.')

        user = self.authenticate_credentials(payload)

        return (user, auth[1])

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        model = get_user_model()

        user_id = payload.get('id', None)
        if not user_id:
            raise exceptions.AuthenticationFailed('Invalid payload')

        try:
            user = model.objects.get(pk=user_id, is_active=True)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid signature')

        return user

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return 'JWT realm="{0}"'.format(self.www_authenticate_realm)
