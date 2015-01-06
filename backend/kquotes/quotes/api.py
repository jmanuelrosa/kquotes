from kquotes.base.api import viewsets
from . import models
from . import serializers


class QuotesViewSet(viewsets.ModelCrudViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

    def get_queryset(self):
        orgs_id_list = self.request.user.memberships.values_list("organization", flat=True)
        return self.queryset.filter(organization__in=orgs_id_list)
