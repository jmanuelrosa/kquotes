from kquotes.base.api import viewsets
from . import models
from . import serializers


class OrganizationsViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class MembersViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
