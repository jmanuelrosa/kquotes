import jwt
from datetime import datetime
import uuid

from django.conf import settings


def payload_handler(user):
    username = user.username

    payload = {
        'username': user.username,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload['username'] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if settings.JWT_AUDIENCE is not None:
        payload['aud'] = settings.JWT_AUDIENCE

    if settings.JWT_ISSUER is not None:
        payload['iss'] = settings.JWT_ISSUER

    return payload


def encode_handler(payload):
    return jwt.encode(payload,
                      settings.JWT_PRIVATE_KEY or settings.SECRET_KEY,
                      settings.JWT_ALGORITHM).decode('utf-8')


def decode_handler(token):
    options = {
        'verify_exp': settings.JWT_VERIFY_EXPIRATION,
    }

    return jwt.decode(token,
                      settings.JWT_PUBLIC_KEY or settings.SECRET_KEY,
                      settings.JWT_VERIFY,
                      options=options,
                      leeway=settings.JWT_LEEWAY,
                      audience=settings.JWT_AUDIENCE,
                      issuer=settings.JWT_ISSUER,
                      algorithms=[settings.JWT_ALGORITHM])
