from kquotes.base.api import viewsets
from . import models
from . import serializers


class UsersViewSet(viewsets.ModelCrudViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
