from kquotes.base.api import viewsets
from . import models
from . import serializers


class OrganizationsViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer

    def get_queryset(self):
        orgs_id_list = self.request.user.memberships.values_list("organization", flat=True)
        return self.queryset.filter(id__in=orgs_id_list)


class MembersViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
