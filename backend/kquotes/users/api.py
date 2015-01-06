from kquotes.base.api import viewsets

from . import models
from . import serializers
from . import services


class UsersViewSet(viewsets.ModelCrudViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        orgs_id_list = self.request.user.memberships.values_list("organization", flat=True)
        return self.queryset.filter(memberships__organization__in=orgs_id_list).distinct()


from kquotes.base.api import permissions

from rest_framework import status
from rest_framework.response import Response


class AuthTokenViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self, request, **kwargs):
        username = request.DATA.get('username', None)
        password = request.DATA.get('password', None)

        user = services.get_and_validate_user(username, password)
        data = serializers.UserAuthTokenSerializer(user).data

        return Response(data, status=status.HTTP_200_OK)
