from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_admin=False):
        """
        Creates and saves a User with the given username, email,
        and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_admin=is_admin
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username, email,
        and password.
        """
        return self.create_user(username, email, password=password, is_admin=True)


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, blank=False,
                                validators=[UnicodeUsernameValidator()],
                                error_messages={
                                    'unique': _("A user with that username already exists.")
                                },
                                verbose_name=_('username'),
                                help_text=_('Required. 150 characters or fewer. Letters, digits '
                                            'and @/./+/-/_ only.'))
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')

    first_name = models.TextField(blank=True, verbose_name=_('first name'))
    last_name = models.TextField(blank=True, verbose_name=_('last name'))

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return ' '.join([self,first_name, self.last_name]) or self.username

    def get_short_name(self):
        return self.first_name or self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
