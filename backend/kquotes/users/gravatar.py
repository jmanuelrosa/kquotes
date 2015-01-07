import hashlib
import copy

from urllib.parse import urlencode

from django.conf import settings
from django.templatetags.static import static

GRAVATAR_BASE_URL = "//www.gravatar.com/avatar/{}?{}"


def get_gravatar_url(email: str, **options) -> str:
    """Get the gravatar url associated to an email.

    :param options: Additional options to gravatar.
    - `default` defines what image url to show if no gravatar exists
    - `size` defines the size of the avatar.

    :return: Gravatar url.
    """

    params = copy.copy(options)

    default_avatar = getattr(settings, "GRAVATAR_DEFAULT_AVATAR", None)
    default_size = getattr(settings, "GRAVATAR_AVATAR_SIZE", None)

    if default_avatar:
        params["default"] = static(default)

    if default_size:
        params["size"] = default_size

    email_hash = hashlib.md5(email.lower().encode()).hexdigest()
    url = GRAVATAR_BASE_URL.format(email_hash, urlencode(params))

    return url
