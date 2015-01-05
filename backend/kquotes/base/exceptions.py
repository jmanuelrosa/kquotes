from rest_framework import exceptions
from rest_framework import status

from django.utils.translation import ugettext_lazy as _
from django.http import Http404



class BaseException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Unexpected error")

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail


class NotFound(BaseException, Http404):
    """
    Exception used for not found objects.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Not found.")


class NotSupported(BaseException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = _("Method not supported for this endpoint.")


class BadRequest(BaseException):
    """
    Exception used on bad arguments detected
    on api view.
    """
    default_detail = _("Wrong arguments.")


class WrongArguments(BadRequest):
    """
    Exception used on bad arguments detected
    on service. This is same as `BadRequest`.
    """
    default_detail = _("Wrong arguments.")


class RequestValidationError(BadRequest):
    default_detail = _("Data validation error")


class IntegrityError(BadRequest):
    default_detail = _("Integrity Error for wrong or invalid arguments")


class PreconditionError(BadRequest):
    """
    Error raised on precondition method on viewset.
    """
    default_detail = _("Precondition error")


class PermissionDenied(exceptions.PermissionDenied):
    """
    Compatibility subclass of restframework `PermissionDenied`
    exception.
    """
    pass


class NotAuthenticated(exceptions.NotAuthenticated):
    """
    Compatibility subclass of restframework `NotAuthenticated`
    exception.
    """
    pass
