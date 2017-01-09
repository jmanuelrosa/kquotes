from __future__ import unicode_literals
from datetime import datetime
import importlib

import jwt


def generate_payload(user):
    from . import settings

    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return {
        'id': user.pk,
        'email': user.email,
        'username': username,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }


def encode(payload):
    from . import settings

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM
    ).decode('utf-8')


def decode(token):
    from . import settings

    options = {
        'verify_exp': settings.JWT_VERIFY_EXPIRATION,
    }

    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        settings.JWT_VERIFY,
        options=options,
        leeway=settings.JWT_LEEWAY
    )
