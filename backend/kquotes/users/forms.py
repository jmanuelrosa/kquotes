from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm

from .models import User


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User


class UserChangeForm(DjangoUserChangeForm):
    class Meta(DjangoUserChangeForm.Meta):
        model = User
