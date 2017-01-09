import datetime
import importlib

from django.conf import settings

def import_from_string(val, module_name='JWT'):
    """
    Attempt to import a class from a string representation.
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        msg = "Could not import '%s' for '%s' setting. %s: %s." % (val, module_name, e.__class__.__name__, e)
        raise ImportError(msg)


JWT_ENCODE_HANDLER = getattr(
    settings,
    'JWT_ENCODE_HANDLER',
    import_from_string('kquotes.auth.jwt.token.encode')
)

JWT_DECODE_HANDLER = getattr(
    settings,
    'JWT_DECODE_HANDLER',
    import_from_string('kquotes.auth.jwt.token.decode')
)

JWT_GENERATE_PAYLOAD_HANDLER = getattr(
    settings,
    'JWT_GENERATE_PAYLOAD_HANDLER',
    import_from_string('kquotes.auth.jwt.token.generate_payload')
)

JWT_SECRET_KEY = getattr(
    settings,
    'JWT_SECRET_KEY',
    settings.SECRET_KEY
)

JWT_ALGORITHM = getattr(settings, 'JWT_ALGORITHM', 'HS256')

JWT_VERIFY = getattr(settings, 'JWT_VERIFY', True)

JWT_VERIFY_EXPIRATION = getattr(settings, 'JWT_VERIFY_EXPIRATION', True)

JWT_LEEWAY = getattr(settings, 'JWT_LEEWAY', 0)

JWT_EXPIRATION_DELTA = getattr(
    settings,
    'JWT_EXPIRATION_DELTA',
    datetime.timedelta(seconds=300)
)

JWT_ALLOW_REFRESH = getattr(settings, 'JWT_ALLOW_REFRESH', False)

JWT_REFRESH_EXPIRATION_DELTA = getattr(
    settings,
    'JWT_REFRESH_EXPIRATION_DELTA',
    datetime.timedelta(seconds=300)
)

JWT_AUTH_HEADER_PREFIX = getattr(settings, 'JWT_AUTH_HEADER_PREFIX', 'Bearer')
