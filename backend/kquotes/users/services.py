from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from kquotes.base import exceptions as exc


def get_and_validate_user(username, password):
    user_model = get_user_model()
    qs = user_model.objects.filter(Q(username=username) |
                                   Q(email=username))
    if len(qs) == 0:
        raise exc.WrongArguments(_("Username, email or password does not matches user."))

    user = qs[0]
    if not user.is_active:
        raise exc.WrongArguments(_("User account is disabled."))

    if not user.check_password(password):
        raise exc.WrongArguments(_("Username email or password does not matches user."))

    return user
