from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.core import validators
from django.utils import timezone

import re


class PermissionsMixin(models.Model):
    '''
    A mixin class that adds the fields and methods necessary to support
    Django's Permission model using the ModelBackend.
    '''
    is_superuser = models.BooleanField(_('superuser status'), default=False,
                                       help_text=_('Designates that this user has all permissions without '
                                                   'explicitly assigning them.'))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    class Meta:
        abstract = True

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_superuser

    def has_perms(self, perm_list, obj=None):
        return self.is_active and self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_active and self.is_superuser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)
    full_name = models.CharField(null=False, blank=True, max_length=256, verbose_name=_('full name'))
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name or self.username or self.email
